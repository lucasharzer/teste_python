from sql_alchemy import banco

class ModeloConta(banco.Model):
    __tablename__ = 'conta'

    conta_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'conta_id': self.conta_id,
            'login': self.login,
            }

    @classmethod
    def encontrar_conta(cls, conta_id):
        conta = cls.query.filter_by(conta_id=conta_id).first()
        if conta:
            return conta
        return None

    @classmethod
    def encontrar_pelo_login(cls, login):
        conta = cls.query.filter_by(login=login).first()
        if conta:
            return conta
        return None

    def salvar_conta(self):
        banco.session.add(self)
        banco.session.commit()

    def deletar_conta(self):
        banco.session.delete(self)
        banco.session.commit()
