import os
import tempfile
from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash
from download_reel import download_reel

app = Flask(__name__, static_folder="static", template_folder="templates")
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

    # Cria um diretório temporário
    temp_dir = tempfile.mkdtemp()
    try:
        # Baixa o reel para temp_dir
        download_reel(url, temp_dir)
        # Encontra o .mp4
        for nome in os.listdir(temp_dir):
            if nome.lower().endswith(".mp4"):
                # Envia como anexo; o browser abrirá “Salvar como…”
                return send_from_directory(
                    directory=temp_dir,
                    filename=nome,
                    as_attachment=True,
                    attachment_filename=nome
                )
        # Se não encontrar .mp4, mostra erro
        flash("❌ Erro: não encontrei o arquivo de vídeo.", "error")
        return redirect(url_for("index"))
    except Exception as e:
        flash(f"❌ Erro ao baixar: {e}", "error")
        return redirect(url_for("index"))
    finally:
        # (Opcional) Se quiser limpar depois, você pode agendar uma limpeza periódica do /tmp
        pass

if __name__ == "__main__":
    app.run(debug=True)