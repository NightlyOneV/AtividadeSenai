from datetime import datetime
import pytz

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
        self.Saldo_Guardado = 0
        self.Agencia = agencia
        self.Numero = numero
        self.transacoes = []
        
    def consultar_historico_trans(self):
        print("\nHISTÓRICO DE TRANSAÇÕES\n")
        for transacao in self.transacoes:
            print(transacao)    
    
    def sacarDinheiro(self, quantidade):
        if quantidade <= self.Saldo_Guardado:
            self.Saldo_Guardado -= quantidade
            self.Saldo += quantidade
            self.transacoes.append(("Saque", quantidade, self.Saldo, self.Saldo_Guardado, ContaCorrente._dataHora()))
        else: print("Saldo insuficiente!")
            
    def depositarDinheiro(self, quantidade):
        if quantidade <= self.Saldo:
            self.Saldo -= quantidade 
            self.Saldo_Guardado += quantidade 
            self.transacoes.append(("Depósito", quantidade, self.Saldo, self.Saldo_Guardado, ContaCorrente._dataHora()))
        else: print("Saldo insuficiente!")
    
    def printarInfo(self):
        print(self.retornarInformação())
    
    def retornarInformação(self):
        return (f"Saldo: {self.Saldo}", f"Saldo guardado: {self.Saldo_Guardado}", f"Nome: {self.Nome}", f"CPF: {self.CPF}")

    def ganharSalario(self, quantidade):
        self.Saldo += quantidade 
    
conta_Lira = ContaCorrente("Lira", "111.222.333-45", "Banco ITAU", "12932193")
conta_maeLira = ContaCorrente("Beth", "222.333.444-55", "Banco INTER", "219312")

conta_Lira.ganharSalario(100)
conta_Lira.printarInfo()
conta_Lira.depositarDinheiro(35)
conta_Lira.depositarDinheiro(35)
conta_Lira.depositarDinheiro(35)
conta_Lira.sacarDinheiro(50)
conta_Lira.printarInfo()
conta_Lira.consultar_historico_trans()

