from flask_restful import Resource, reqparse
from modelos.usuario import ModeloUsuario
from flask_jwt_extended import jwt_required

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
        return {'usuarios': [usuario.json() for usuario in ModeloUsuario.query.all()]}

class Usuario(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="the field 'nome' is required")
    argumentos.add_argument('idade', type=float, required=True, help="the field 'idade' is required")
    argumentos.add_argument('cidade', type=str, required=True, help="the fiel 'cidade' is required")

    def get(self, usuario_id):
        usuario = ModeloUsuario.encontrar_usuario(usuario_id)
        if usuario:
            return usuario.json()
        return {'message': 'User not found.'}, 404
    
    @jwt_required()
    def post(self, usuario_id):
        if ModeloUsuario.encontrar_usuario(usuario_id):
            return {"message": "User id '{}' already exists.".format(usuario_id)}, 400 

        dados = Usuario.argumentos.parse_args()
        usuario = ModeloUsuario(usuario_id, **dados)
        try:
            usuario.salvar_usuario()
        except:
            return {"message": "An internal error ocurred trying to save user."}, 500
        return usuario.json()

    @jwt_required()
    def put(self, usuario_id):
        dados = Usuario.argumentos.parse_args()
        usuario_encontrado = ModeloUsuario.encontrar_usuario(usuario_id)
        if usuario_encontrado:
            usuario_encontrado.atualizar_usuario(**dados)
            usuario_encontrado.salvar_usuario()
            return usuario_encontrado.json() , 200 
        usuario = ModeloUsuario(usuario_id, **dados)
        try:
            usuario.salvar_usuario()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 # Internal Server Error
        return usuario.json(), 201 # created criado

    @jwt_required()
    def delete(self, usuario_id):
        usuario = ModeloUsuario.encontrar_usuario(usuario_id)
        if usuario:
            try:
                usuario.deletar_usuario()
            except:
                return {'message': 'An error occured trying to delete user.'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404