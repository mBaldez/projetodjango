## Projeto Django - Courses

Este é um projeto Django criado para estudo/avaliação. Ele contém páginas HTML renderizadas com views e URLs básicas.

## Pré-requisitos

- Python 3.x instalado
- Git (opcional, se for clonar do GitHub)

## Configuração do ambiente

1. Clone o repositório (ou baixe os arquivos):

```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio


Crie um ambiente virtual:

Windows:

python -m venv venv
.\venv\Scripts\activate


Linux/Mac:

python -m venv venv
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Se não houver requirements.txt, você pode instalar Django manualmente:

pip install django

Executando o projeto

No terminal, dentro da pasta do projeto (onde está o manage.py), rode:

python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000/


Agora você verá as páginas HTML do projeto.

Estrutura do projeto

manage.py → arquivo principal do Django

meuprojeto/ → configuração do projeto Django

myapp/ → app com views, templates e URLs

myapp/templates/ → arquivos HTML

README.md → este arquivo

LICENSE → licença do projeto

Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.


---

💡 **Dicas finais:**
1. Salve este arquivo como `README.md` na raiz do projeto.  
2. Crie ou atualize o `requirements.txt` com:

```bash
pip freeze > requirements.txt


Depois envie para o GitHub:

git add README.md LICENSE requirements.txt
git commit -m "Adiciona README, LICENSE e requirements"
git push