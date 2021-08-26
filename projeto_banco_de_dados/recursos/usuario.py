from flask_restful import Resource, reqparse
from modelos.usuario import ModeloUsuario

usuarios = [
    {
        'usuario_id': 'primeiro',
        'nome': 'Ana',
        'idade': 45,
        'cidade': 'Rio de Janeiro'
    },
    {
        'usuario_id': 'segundo',
        'nome': 'Bob',
        'idade': 23,
        'cidade': 'São Paulo'
    },
    {
        'usuario_id': 'terceiro',
        'nome': 'Eduardo',
        'idade': 11,
        'cidade': 'Santa Catarina'
    }
]

class Usuarios(Resource):
    def get(self):
        return {'usuarios': usuarios}

class Usuario(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('idade')
    argumentos.add_argument('cidade')

    def encontrar_usuario(usuario_id):
        for usuario in usuarios:
            if usuario['usuario_id'] == usuario_id:
                return usuario
        return False

    def get(self, usuario_id):
        usuario = Usuario.encontrar_usuario(usuario_id)
        if usuario:
            return usuario
        return {'message': 'User not found.'}, 404
    
    def post(self, usuario_id):
        dados = Usuario.argumentos.parse_args()
        usuario_objeto = ModeloUsuario(usuario_id, **dados)
        novo_usuario = usuario_objeto.json()
        usuarios.append(novo_usuario)
        return novo_usuario, 200 

    def put(self, usuario_id):
        dados = Usuario.argumentos.parse_args()
        usuario_objeto = ModeloUsuario(usuario_id, **dados)
        novo_usuario = usuario_objeto.json()
        usuario = Usuario.encontrar_usuario(usuario_id)
        if usuario:
            usuario.update(novo_usuario)
            return novo_usuario, 200 
        usuarios.append(novo_hotel)
        return novo_usuario, 201

    def delete(self, usuario_id):
        global usuarios # se refere a lista de hoteis
        usuarios = [usuario for usuario in usuarios if usuario['usuario_id'] != usuario_id]
        return {'message': 'User deleted.'}