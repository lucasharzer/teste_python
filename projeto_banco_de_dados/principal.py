from logging import debug
from flask import Flask
from flask_restful import Api
from recursos.usuario import Usuarios, Usuario

app = Flask(__name__)
api = Api(app)

api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuarios/<string:usuario_id>')
if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/ 