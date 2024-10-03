class ContaCorrente:
    def __init__(self, nome , cpf):
        self.Nome = nome 
        self.CPF = cpf 
        self.Saldo = 0
        self.Saldo_Guardado = 0
        
    def sacarDinheiro(self, quantidade):
        if quantidade <= self.Saldo_Guardado:
            self.Saldo_Guardado -= quantidade
            self.Saldo += quantidade
        else: print("Saldo insuficiente!")
            
    def depositarDinheiro(self, quantidade):
        if quantidade <= self.Saldo:
            self.Saldo -= quantidade 
            self.Saldo_Guardado += quantidade 
        else: print("Saldo insuficiente!")
    
    def retornarInformação(self):
        return (f"Saldo: {self.Saldo}", f"Saldo guardado: {self.Saldo_Guardado}", f"Nome: {self.Nome}", f"CPF: {self.CPF}")

    def ganharSalario(self, quantidade):
        self.Saldo += quantidade 
    
conta_Lira = ContaCorrente("Lira", "111.222.333-45")

conta_Lira.ganharSalario(100)
print(conta_Lira.retornarInformação())
conta_Lira.depositarDinheiro(35)
print(conta_Lira.retornarInformação())

