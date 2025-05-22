from flask import Flask, render_template, request, redirect, url_for, flash
import os
from download_reel import download_reel

app = Flask(__name__, static_folder="static", template_folder="template")
# Mude esta chave para algo secreto em produção
app.secret_key = "uma_senha_aleatoria_para_sessions"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def do_download():
    url = request.form.get("url", "").strip()
    if not url:
        flash("❌ Por favor, insira a URL do Reel.", "error")
        return redirect(url_for("index"))

    # pasta onde vamos salvar
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    try:
        download_reel(url, output_dir)
        flash(f"✅ Reel salvo em `{output_dir}`", "success")
    except Exception as e:
        flash(f"❌ Erro ao baixar: {e}", "error")

    return redirect(url_for("index"))

if __name__ == "__main__":
    # debug=True para recarregar automaticamente ao editar
    app.run(debug=True)