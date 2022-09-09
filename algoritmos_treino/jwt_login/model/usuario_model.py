from util.db import db
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token


class UsuarioModel(db.Model):
    __tablename__ = 'tb_usuario'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    senha = db.Column(db.String(32), nullable=False)


    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


 # API Methods:

    def post(self):
        UsuarioModel.add(self)


# Class methods:

    def add(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_email(cls, email):
        return UsuarioModel.query.filter_by(email=email).first()


class Login():
    def dados_corretos(**dados):

        user = UsuarioModel.find_by_email(dados['email'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            return True

    def gerar_token(**dados):
        user = UsuarioModel.find_by_email(dados['email'])

        token_de_acesso = create_access_token(identity=user.id)
        return {'access_token': token_de_acesso}
