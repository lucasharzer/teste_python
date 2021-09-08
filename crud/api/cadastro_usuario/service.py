USUARIOS_LIST = [
        {
            'usuario_id': 1,
            'nome': 'Ana',
            'idade': 45,
            'cidade': 'Rio de Janeiro'
        },
        {
            'usuario_id': 2,
            'nome': 'Bob',
            'idade': 23,
            'cidade': 'São Paulo'
        },
        {
            'usuario_id': 3,
            'nome': 'Eduardo',
            'idade': 11,
            'cidade': 'Santa Catarina'
        }
    ]

class Usuario():

    def encontrar_usuario(self, usuario_id):
        for usuario in USUARIOS_LIST:
            if usuario['usuario_id'] == int(usuario_id):
                return usuario
        return False

    def get_all_user(self):
        return {'usuarios': USUARIOS_LIST}

    def get_user(self, usuario_id):
        usuario = self.encontrar_usuario(usuario_id)
        if usuario:
            return usuario
        return {'message': 'User not found.'}, 404
    
    # def post_user(self, usuario_id):
    #     dados = self.argumentos.parse_args()
    #     usuario_objeto = ModeloUsuario(usuario_id, **dados)
    #     novo_usuario = usuario_objeto.json()
    #     USUARIOS_LIST.append(novo_usuario)
    #     return novo_usuario, 200 

    # def put(self, usuario_id):
    #     dados = self.argumentos.parse_args()
    #     usuario_objeto = ModeloUsuario(usuario_id, **dados)
    #     novo_usuario = usuario_objeto.json()
    #     usuario = self.encontrar_usuario(usuario_id)
    #     if usuario:
    #         usuario.update(novo_usuario)
    #         return novo_usuario, 200 
    #     USUARIOS_LIST.append(novo_hotel)
    #     return novo_usuario, 201

    # def delete_user(self, usuario_id):
    #     usuario = [usuario for usuario in USUARIOS_LIST if usuario['usuario_id'] != usuario_id]
    #     return {'message': f'User {usuario} deleted.'}