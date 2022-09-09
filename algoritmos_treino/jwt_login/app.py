# Importacoes de arquivos e bibliotecas
import json
from flask import Flask
from flask_cors import CORS
from util.db import db
from flask_jwt_extended import JWTManager


# Configuracoes
config_file = open('config/dev.json') 
config = json.load(config_file)


app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']


# Api's imports:
from api.usuario_api import usuario_api


# Registro das api's no Blueprint
app.register_blueprint(usuario_api)


# Configuração JWT
jwt = JWTManager(app)


# Criacao das tabelas no banco de dados
@app.before_first_request
def create_database():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
