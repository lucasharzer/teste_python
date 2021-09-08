import logging
import os
from jsonschema import FormatChecker

from flask_restplus import Api as _Api
from werkzeug.exceptions import HTTPException

log = logging.getLogger(__name__)

v = os.popen('git log | head -n 1')
commit = v.read().replace("commit ", "")[:7]

api = _Api(
  version = f"0.1#{commit}",
  default = "",
  doc="/docs",
  title = "Cadastro de Usuarios",
  description = "A simple Api",
  format_checker = FormatChecker()
)

@api.errorhandler
def default_error_hajndler(e):
  if isinstance(e, HTTPException):
    response = {"message": e.description}
    status_code = e.code
  else:
    response = {"message": "Unhandled Exception"}
    status_code = 500

  log.exception(e)
  return response, status_code  
