from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from download_reel import download_reel
import os

app = Flask(__name__, static_folder="static", template_folder="template")

app.secret_key = "uma_senha_aleatoria_para_sessions"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/download", methods=["POST"])
def do_download():
    url = request.form.get("url", "").strip()
    if not url:
        flash("❌ Por favor, insira a URL do Reel.", "error")
        return redirect(url_for("index"))

    try:
        # Faz o download e obtém o caminho exato do arquivo
        filepath = download_reel(url, "downloads")
        # Envia para o cliente como anexo
        return send_file(
            filepath,
            as_attachment=True,
            download_name=os.path.basename(filepath)
        )
    except Exception as e:
        flash(f"❌ Erro ao baixar: {e}", "error")
        return redirect(url_for("index"))