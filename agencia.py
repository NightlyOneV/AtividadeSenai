from random import randint

class Agencia:
    def __init__(self, _telefone, _cnpj, _numero):
        self.telefone = _telefone
        self.cnpj = _cnpj
        self.numero = _numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        pass

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O Valor de Caixa está ok. Caixa Atual:{}'.format(self.caixa))

    def emprestar_dinheiro(self, _valor, _cpf, _juros):
        if self.caixa > _valor:
            self.emprestimos.append((_valor, _cpf,_juros))
            print('Emprestimo efetuado')
        else:
            print('Emprestimo não possível. Dinheiro insulficiente.')

    def adicionar_cliente(self, _nome, _cpf, _patrimonio):
        self.clientes.append((_nome,_cpf,_patrimonio))

class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 10000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor 
        self.caixa += valor

class AgenciaComum(Agencia):
    def __init__(self, _telefone, _cnpj):
        super().__init__(_telefone, _cnpj, randint(1001,9999))
        self.caixa=1000000

class AgenciaPremium(Agencia):
    def __init__(self, _telefone, _cnpj):
        super().__init__(_telefone, _cnpj, randint(1001,9999))
        self.caixa=10000000

agencia_comum = AgenciaComum(33334444,222000000000)
agencia_comum.verificar_caixa()
print(agencia_comum.__dict__)
agencia_virtual = AgenciaVirtual("youtube.com", 3943543, 924923)
print(agencia_virtual.__dict__)

agencia_premium = AgenciaPremium(3333333,3000000000000)
print('agencia-premium: ')
print(agencia_premium.__dict__)