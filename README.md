# Como utilizar o Reel Downloader?

Essa é uma aplicação open-source de download de reels do instagram - o intuito é rodar localmente na sua máquina, com apenas um comando. Não tem anúncios chatos e a qualidade do reels é nativa (qualidade em que foi postado).

Para fazer esse projeto, eu utilizei a lib yt_dlp e o flask como servidor - após rodar o comando 'flask run' um servidor é aberto com uma página HTML/CSS.

## Installation

Crie um ambiente virtual .venv

```bash
python -m venv nome_do_ambiente
```
Inicie o .venv
```bash
source meu_ambiente_virtual/bin/activate
```

Use o comando [pip](https://pip.pypa.io/en/stable/) para instalar os pacotes e dependências.

```bash
pip install -r requirements.txt
```

## Como iniciar?

Depois de instalar os pacotes, criar o ambiente e iniciar o venv - digite no terminal o comando:
```bash
flask run
```

## Contributing
Se tiver alguma sugestão - pull requests são bem-vindos - abra um issue primeiro para iniciar uma discussão do que você gostaria de mudar no código.

## License

[MIT](https://choosealicense.com/licenses/mit/)
