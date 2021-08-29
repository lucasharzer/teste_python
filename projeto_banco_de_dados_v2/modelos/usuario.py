from sql_alchemy import banco

class ModeloUsuario(banco.Model):
    __tablename__ = 'usuarios'

    usuario_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(40)) # máximo de caracteres
    idade = banco.Column(banco.Float(precision=0))
    cidade = banco.Column(banco.String(40))


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
    
    @classmethod
    def encontrar_usuario(cls, usuario_id):
        usuario = cls.query.filter_by(usuario_id=usuario_id).first()
        if usuario:
            return usuario
        return None

    def salvar_usuario(self):
        banco.session.add(self)
        banco.session.commit()
    
    def atualizar_usuario(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def deletar_usuario(self):
        banco.session.delete(self)
        banco.session.commit()
