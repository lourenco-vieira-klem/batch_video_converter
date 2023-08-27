import sys
import ffmpeg
from marshmallow import Schema, fields, validate
from custom_errors import ConfigError, CustomError


class KeyArgsSchema(Schema):
    fps = fields.Integer(required=True, validate=[validate.OneOf([24, 30, 30, 60, 120])])
    encoder = fields.String(required=True, validate=[validate.OneOf(['h264_nvenc', 'av1_nvenc'])])
    bitrate = fields.Integer(required=True)
    inputfile = fields.String(required=True)
    outputfile = fields.String(required=True)
    format = fields.String(required=True, validate=[validate.OneOf(['mp4', 'mkv', 'avi'])])

class VideoConverter():
    def __init__(self, video_path: str, encoded_archive_name: str, encoder: str, bitrate: int, fps = int) -> None:
        self.video_path = video_path
        self.encoded_archive_name = encoded_archive_name
        self.encoder = encoder
        self.bitrate = bitrate
        self.fps = fps
    
    def convert_video(self) -> None:
        input_video = ffmpeg.input(self.video_path)
        input_video = ffmpeg.output(
            input_video,
            self.encoded_archive_name,
            **{'r': self.fps, 'c:v': self.encoder, 'b:v': f'{self.bitrate}k'}
        )
        input_video = ffmpeg.run(input_video)
    
    def run(self):
        self.convert_video()
    
if __name__ == '__main__':
    try:
        argv= sys.argv[1:] 
        kwargs={kw[0]:kw[1] for kw in [ar.split('=') for ar in argv if ar.find('=')>0]}
        
        schema = KeyArgsSchema()
        errors = schema.validate(kwargs)
        if errors:
            raise ConfigError(message=str(errors))
        
        task = VideoConverter(
            video_path=kwargs['inputfile'],
            encoded_archive_name=f"{kwargs['outputfile']}.{kwargs['format']}",
            encoder=kwargs['encoder'],
            bitrate=kwargs['bitrate'],
            fps=kwargs['fps']
        )
        
        task.run()
        
    except CustomError as ex:
        print(ex.message)
    
    except Exception as ex:
        print(ex)
