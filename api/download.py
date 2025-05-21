import os
import tempfile
from flask import Flask, request, send_file

from download_reel import download_reel

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_endpoint():
    url = request.form.get("url", "").strip()
    if not url:
        return "URL do Reel não informada", 400

    # cria pasta temporária para download
    tmp = tempfile.mkdtemp()
    try:
        download_reel(url, tmp)
        # encontra o .mp4 gerado
        for fn in os.listdir(tmp):
            if fn.lower().endswith(".mp4"):
                path = os.path.join(tmp, fn)
                return send_file(
                    path,
                    as_attachment=True,
                    download_name=fn
                )
        return "Vídeo não encontrado no diretório", 500
    except Exception as e:
        return f"Erro ao baixar: {e}", 500