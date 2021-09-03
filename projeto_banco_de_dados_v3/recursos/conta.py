from flask_restful import Resource, reqparse
from modelos.conta import ModeloConta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")

class Conta(Resource):

    # /usuarios/{user_id}
    def get(self, conta_id):
        conta = ModeloConta.encontrar_conta(conta_id)
        if conta:
            return conta.json()
        return {'message': 'User not found.'}, 404 

    @jwt_required()
    def delete(self, conta_id):
        conta = ModeloConta.encontrar_conta(conta_id)
        if conta:
            conta.deletar_conta()
            return {'message': 'User deleted.'}
        return {'message': 'Account not found.'}, 404

class RegistrarConta(Resource):
    # /cadastro
    def post(self):
        dados = atributos.parse_args()

        if ModeloConta.encontrar_pelo_login(dados['login']):
            return {"message": "The login '{}' already exists.".format(dados['login'])}
        
        conta = ModeloConta(**dados)
        conta.salvar_conta()
        return {'message': 'User created successfully!'}, 201 # Created

class LoginConta(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        conta = ModeloConta.encontrar_pelo_login(dados['login'])

        if conta and safe_str_cmp(conta.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=conta.conta_id)
            return {'acess_token': token_de_acesso}, 200
        return {'message': 'The account or password is incorrect.'}, 401 # Unauthorized


class LogoutConta(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] # JWT Token Identifier
        BLACKLIST.add(jwt_id)
        return {'massage': 'Logged out successfully!'}, 200
