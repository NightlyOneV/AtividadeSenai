import math
import random

def Att1():
    class Circulo:
        def __init__(self, _Raio):
            self.Raio = _Raio
            print("INICIADO")

        def CalcPerimetro(self):
            return (2 * math.pi * self.Raio)

        def CalcArea(self):
            return (math.pi * self.Raio ** 2)
        
    Circ = Circulo(10)
    print(Circ.CalcArea())
    print(Circ.CalcPerimetro())

def Att2():
    class ContaBancaria():
        def __init__(self, nomeTitular, saldoInicial):
            self.Nome = nomeTitular
            self.Saldo = saldoInicial
            self.numeroConta = random.randint(1000, 9999)
        
        def depositar(self, Quantia):
            self.Saldo += Quantia
            print(f"{self.Nome}, você Depositou R${Quantia}, seu saldo agora é: R${self.Saldo - Quantia}") 

        def sacar(self, Quantia):
            if self.Saldo < Quantia:
                print("Saldo insuficiente para sacar!")
            else:
                self.Saldo -= Quantia
                print(f"{self.Nome}, você sacou R${Quantia}, seu saldo agora é de R${self.Saldo}")

    Conta = ContaBancaria("José", 5000)
    Conta.depositar(150)
    Conta.sacar(4000)
    Conta.depositar(200)
    Conta.sacar(7000)

def Att3():
    class retangulo:
        def __init__(self,altura,largura):
            self.largura = largura 
            self.altura = altura
            self.area = None 
            self.perim = None

        def calArea(self):
            self.area = self.largura * self.altura
            return self.area
        
        def calperim(self):
            self.perim = 2 * (self.largura + self.altura)
            return self.perim
        
        def info(self):
            print(f"Retângulo: Largura = {self.largura}, Altura = {self.altura}")
            print(f"Área: {self.area}")
            print(f"perimetro :{self.perim}")

    retangulo1 = retangulo(5,4)
    retangulo1.calArea()
    retangulo1.calperim()
    print(retangulo1.info())

def Att4():
    class criar_aluno:
        def __init__(self,_nome,_matricula):
            self.nome = _nome
            self.matricula = _matricula
            self.notas = [0,0,0]

        def add_nota(self,_nota):
            nota = _nota
            self.notas = nota

        def calc_media(self):
            self.media = (self.notas[0] + self.notas[1] + self.notas[2]) / 3 
            return self.media
        
    zezé = criar_aluno("José","2210")
    zezé.add_nota([10,4,8])
    print(zezé.calc_media())

def Att5():
    class Funcionario():
        def __init__(self, nomeFun, Salario, Cargo):
            self.Nome = nomeFun
            self.Salario = Salario
            self.Cargo = Cargo
            print("Funcionário cadastrado com sucesso!")

        def CalculandoSalarioLiquido(self):
            Imposto = 0.8 # - 20%

            print(f"{self.Nome} ({self.Cargo}) tem um salário líquido de {self.Salario * Imposto}")

    Func = Funcionario("Fulano", 1500, "Profissional")
    Func.CalculandoSalarioLiquido()

def Att6():
    class Produto:
        def __init__(self, nome, preco, quantidade_em_estoque):
            self.nome = nome
            self.preco = preco
            self.quantidade_em_estoque = quantidade_em_estoque
        
        def valor_total_em_estoque(self):
            return self.preco * self.quantidade_em_estoque
    
        def esta_disponivel(self):
            return self.quantidade_em_estoque > 0

    produto = Produto("Laptop", 2000.00, 10 )
    print("Valor TOTAL DO ESTOE:", produto.valor_total_em_estoque())
    print("Produto está disponível?")
    if produto.esta_disponivel():
        print("Sim!")
    else:
        print("NÃO!")

def Att7():
    class Triangulo:
        def __init__(self, l1, l2, l3):
            self.Lado1 = l1
            self.Lado2 = l2
            self.Lado3 = l3
            self.Validar()

        def Validar(self):
            if (self.Lado1 + self.Lado2 > self.Lado3) and (self.Lado1 + self.Lado3 > self.Lado2) and (self.Lado2 + self.Lado3 > self.Lado1):
                print("O triângulo é válido!")
                self.CalcularArea()
            else:
                print("Os lados não formam um triângulo válido.")

        def CalcularArea(self):
            Soma = (self.Lado1 + self.Lado2 + self.Lado3) / 2
            self.Area = math.sqrt(Soma * (Soma - self.Lado1) * (Soma - self.Lado2) * (Soma - self.Lado3))
            print(f"A área do triângulo é {self.Area}")

    T = Triangulo(10, 10, 10)

def Att8():
    class criar_carro:
        def __init__(self,_marca,_modelo):
            self.marca = _marca
            self.modelo = _modelo
            self.spd = 0

        def acelerar(self, _add):
            self.spd += _add

        def desacelerar(self,_add):
            self.spd -= _add

        def vel_atual(self):
            return self.spd
    
    carro1 = criar_carro("Motorola", "Maneiro")
    carro1.acelerar(10)
    carro1.desacelerar(5)
    print(carro1.vel_atual())

def Att9():
    class Paciente:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
            self.historico_consultas = []
        
        def adicionar_consulta(self, data, descricao):
            consulta = {"data": data, "descricao": descricao}
            self.historico_consultas.append(consulta)
        
        def exibir_consultas(self):
            if not self.historico_consultas:
                print(f"{self.nome} não possui consultas registradas.")
            else:
                print(f"Histórico de consultas de {self.nome}:")
                for consulta in self.historico_consultas:
                    print(f"Data: {consulta['data']}, Descrição: {consulta['descricao']}")

    paciente = Paciente("Maria Silva", 65)
    paciente.adicionar_consulta("2023-07-15", "Consulta de rotina")
    paciente.adicionar_consulta("2023-08-05", "Retorno para resultados de exames")

    paciente.exibir_consultas()

def Att10():
    class livro:
        def __init__(self,titulo,autor,Num_paginas):
            self.titulo = titulo
            self.autor = autor
            self.Num_paginas = Num_paginas
            self.disponivel = True

        def  emprestar(self):
        
            if self.disponivel:
                self.disponivel = False
                print(f"O livro '{self.titulo}' foi emprestado.")
            else:
                print(f"O livro '{self.titulo}' não está disponível no momento.")
        def devolver(self):
            if not self.disponivel:
                self.disponivel = True
                print(f"O livro '{self.titulo}' foi devolvido.")
            else:
                print(f"O livro '{self.titulo}' já está disponível.")
        def verificar_disponibilidade(self):
            return self.disponivel
        def info(self):
            estado = "disponível" if self.disponivel else "emprestado"
            print(f"Livro: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.Num_paginas}\nEstado: {estado}")        
    
    livro1 = livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1216)

    livro1.info()  
    livro1.info()  
    livro1.devolver() 
    livro1.info()

# Seleção da atividade
Att7()