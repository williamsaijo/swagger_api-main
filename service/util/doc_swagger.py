from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    #'textoMensagem': fields.List(fields.String(), required=True, description= "Frase em inglês a ser classificada")})
    'n1': fields.List(fields.Integer(), required=True, description= "1° numero a ser somado"),
    'n2': fields.List(fields.Integer(), required=True, description= "2° numero a ser somado")
})

