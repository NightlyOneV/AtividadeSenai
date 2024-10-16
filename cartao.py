from datetime import datetime
import pytz
from random import randint
class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.Numero = randint(10000, 99999)
        self.Titular = titular
        self.Validade = "{}/{}".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_Seguranca =  "{}{}{}".format(randint(0,9), randint(0,9), randint(0,9))
        self.Limite = None 
        self.conta_corrente = conta_corrente
        conta_corrente.Cartoes.append(self)