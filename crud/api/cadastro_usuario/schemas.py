from marshmallow import Schema, fields

class UserSchema(Schema):
    usuario_id = fields.Integer(description="ID do usuario", required=True)
    nome = fields.String(description="Nome do Usuario", required=True)
    idade = fields.String(description="Idade do usuario", required=True)
    cidade = fields.String(description="Cidade do usuario", required=True)
