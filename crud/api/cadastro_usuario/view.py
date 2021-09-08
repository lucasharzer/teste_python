from crud.api import api
from crud.api.cadastro_usuario.service import Usuario
from crud.api.cadastro_usuario.schemas import UserSchema

from flask_restplus import Resource
from flask import request

import logging

log = logging.getLogger(__name__)
ns = api.namespace("cadastro", description="Cadastra usuarios.")

@ns.route("/usuario/<string:user_id>")
class Users(Resource):
  @ns.expect(UserSchema, validate=True)
  def get(self, user_id):
    return Usuario().get_user(user_id)

@ns.route("/usuario")
class Users(Resource):
  def get(self):
    return Usuario().get_all_user()
