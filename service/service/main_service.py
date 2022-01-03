import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np


class SentimentosService():

    
    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_MODEL)
        self.load_model()

    def load_model(self):

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_rest(self, res):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts = self.buscar_predicao(res['n1'],res['n2'])

        response = {
                     "Resultado da Soma": response_predicts}

        return response

    def buscar_predicao(self,n1,n2):
            logger.debug('Iniciando o calculo...')
        #class  soma2numeros():
            #n1 = int(input('Digite um numero = '))
            #n2 = int(input('Digite outro numero = '))
            response = n1[0] + n2[0]
            print(response)
            print('A soma entre {} e {} é {}!'.format(n1,n2,response))
        
            return response
        
