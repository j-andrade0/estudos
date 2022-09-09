from flask import Blueprint
import controller.usuario_controller as controller


usuario_api = Blueprint('usuario_api', __name__)


@usuario_api.route('/usuario', methods=['POST'])
def post():
    return controller.post()


# Login de usuario

@usuario_api.route('/login', methods=['POST'])
def login():
    return controller.login()
