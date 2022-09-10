# Informações sobre o projeto:
    Projeto feito para atividade de autenticação com JWT, possuindo apenas cadastro de usuário e login,
    onde é verificado se as informações batem com o que foi previamente cadastradas no banco de dados PostgreSQL.

## Ferramentas necessárias: 
    Backend:
        PostgreSQL, Python 3x (libs necessárias estão no arquivo requirements.txt).
    Frontend:

## Como executar:
    Em config/dev.json altere o usuário e senha do PostgreSQL no valor do campo SQLALCHEMY_DATABASE_URI onde estão destacados em maiúsculo: 
    USUARIO:SENHA.
    
    Na pasta do projeto, instale as libs com o comando (se preferir, utilize o VirtualEnv para separar das libs locais): 
    pip install -r requirements.txt

    Execute jwt_login/app.py.

    O backend já estará rodando na rota http://127.0.0.1:5000/login para login e http://127.0.0.1:5000/usuario para cadastro de usuário.

## Campos necessários para cadastro de usuário:
    nome(string)
    email(string)
    senha(string)

## Campos necessários para login:
    email(string)
    senha(string)

## Respostas da API:
    http://127.0.0.1:5000/usuario deverá retornar status code 201 e a mensagem "msg: Usuario criado"

    http://127.0.0.1:5000/login deverá retornar status code 200 e a mensagem "acess_token: " seguido da String contendo o token de acesso gerado pelo backend da aplicação
