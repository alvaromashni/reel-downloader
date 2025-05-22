#!/usr/bin/env python3
"""
download_reel.py
Faz download de um Reel público do Instagram como MP4 compatível,
usando yt-dlp, e retorna o caminho do arquivo gerado.
"""
import os
from yt_dlp import YoutubeDL

def download_reel(url: str, output_dir: str) -> str:
    # Garante que a pasta exista
    os.makedirs(output_dir, exist_ok=True)

    # Configurações para baixar em MP4
    ydl_opts = {
        "format": "mp4",
        "outtmpl": os.path.join(output_dir, "%(id)s.%(ext)s"),
        # você pode descomentar para ver logs detalhados:
        # "verbose": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # prepare_filename usa as mesmas regras de outtmpl
        filename = ydl.prepare_filename(info)

    return filename