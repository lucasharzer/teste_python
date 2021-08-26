class ModeloUsuario:
    def __init__(self, usuario_id, nome, idade, cidade):
        self.usuario_id = usuario_id
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def json(self):
        return {
            'usuario_id': self.usuario_id,
            'nome': self.nome,
            'idade': self.idade,
            'cidade': self.cidade
        }