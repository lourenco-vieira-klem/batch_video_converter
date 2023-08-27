# BATCH VIDEO CONVERTER

Script útil para conversão de arquivos de vídeo.

## Criação do ambiente virtual.

```bash
pipenv install -r requirements.txt
```
```bash
pipenv shell
```

## Execute o comando abaixo para realizar a conversão do arquivo de vídeo desejado.

```bash
python main.py fps=300 encoder=av1_nvenc bitrate=2500 inputfile=C:\Users\exemplodeusuario\Videos\video_input.mp4 outputfile=video_output format=mkv

## fps: pode ser um dos valores (24, 30, 30, 60, 120).
## encoder: pode ser um dos valores (h264_nvenc ou av1_nvenc).
## bitrate: um valor inteiro.
## inputfile: caminho do arquivo de entrada.
## outputfile: caminho e nome do arquivo sem a extenção (C:\Users\exemplodeusuario\Videos\pasta\arquivodesaida).
## format: pode ser um dos valores (mp4, mkv ou avi).
```
## A lib ffmpeg fornece um log detalhado com todas as informações e status da conversão.
