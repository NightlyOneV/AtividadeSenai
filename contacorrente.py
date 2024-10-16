from datetime import datetime
import pytz
from random import randint
class ContaCorrente:
    
    @staticmethod
    def _dataHora():
        fuso_br = pytz.timezone("Brazil/East")
        horario_br = datetime.now(fuso_br).strftime("%d/%m/%y, %H:%M:%S")
        return horario_br
    
    def __init__(self, nome , cpf, agencia, numero):
        self.Nome = nome 
        self.CPF = cpf 
        self.Saldo = 0
        self.Agencia = agencia
        self.Numero = numero
        self.transacoes = []
        self.Cartoes = []
        
    def consultar_historico_trans(self):
        print("\nHISTÓRICO DE TRANSAÇÕES\n")
        for transacao in self.transacoes:
            print(transacao)    
            
    def depositarDinheiro(self, quantidade):
        self.Saldo += quantidade 
        self.transacoes.append(("Depósito", quantidade, self.Saldo, ContaCorrente._dataHora()))
    
    def printarInfo(self):
        print(self.retornarInformação())
    
    def retornarInformação(self):
        return (f"Saldo: {self.Saldo}",  f"Nome: {self.Nome}", f"CPF: {self.CPF}")

    def ganharSalario(self, quantidade):
        self.Saldo += quantidade 
        self.transacoes.append(("Salário", quantidade, self.Saldo, ContaCorrente._dataHora()))
#    ANWQX