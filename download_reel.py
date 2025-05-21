#!/usr/bin/env python3
"""
download_reel.py
Contém apenas a lógica de baixar o Reel e, em caso de erro,
lança uma Exception para quem chamar tratar.
"""

from instaloader import Instaloader, Post

def download_reel(url: str, output_dir: str = ".") -> None:
    loader = Instaloader(
        dirname_pattern=output_dir,
        download_comments=False,
        save_metadata=False
    )
    shortcode = url.rstrip("/").split("/")[-1]
    # Se algo der errado aqui, uma Exception será lançada
    post = Post.from_shortcode(loader.context, shortcode)
    loader.download_post(post, target=output_dir)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python download_reel.py <URL_do_Reel> [diretório_de_saida]")
        sys.exit(1)

    url = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) >= 3 else "."

    try:
        download_reel(url, out)
        print(f"✅ Reel salvo em {out}")
    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")