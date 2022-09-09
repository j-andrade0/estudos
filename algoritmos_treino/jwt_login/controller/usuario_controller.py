from flask import request
from model.usuario_model import UsuarioModel as model
from model.usuario_model import Login

# Cadastro de usuário
def post():
    dados = request.get_json()
    usuario = model(**dados)
    usuario.post()
    return {'msg':'Usuario criado'}


# Login de usuario

def login():
    dados = request.get_json()

    if Login.dados_corretos(**dados):
        return Login.gerar_token(**dados)