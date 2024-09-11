
def ex1():
    n = int(input("Digite um número inteiro positivo: "))

    numero = 2
    primo = True

    while(numero <= n-1) and (primo):
        if (n & numero == 0):
            primo = False
        numero = numero + 1

    if(primo):
        print("é primo")
    else:
        print("não é primo")

def ex2():
    n = int (input("Digite um número: "))
    anterior = int(input())

    i = 1
    ordenado = True

    while (i < n) and (ordenado):
        atual = int(input())
        i = i + 1
        if (atual < anterior):
            ordenado = False
        anterior = atual
    
    if (ordenado): 
        print("Sequencia ordenada")
    else: 
        print("Sequencia não ordenada")

def ex3():
    i = [0]
    anterior = 0
    adjacente = False
    for x in range(5):
        atual = int(input("Digite um número: "))
        i.append(atual)
        if (atual == anterior):
            adjacente = True
        anterior = atual
    
    if (adjacente):
        print("Há adjacente")

def exstring1():
    a = "20 de Abril tem prova."
    b = "Fizeram os exercícios?"
    c = a + b

    print(3*c)

def exstring2():
    string = input("Digite um texto: ")
    inversa = ""
    for x in string:
        inversa = x +inversa
    print(inversa)

def exstring3():
    a = "20 de abril tem prova"
    print(a[6:11])
    print(a[6:11:2])
    print(a[::-1])

def exstring4():
    b = "\nFizeram os exercícios?\n"
    print(b.strip(),"Oi")

def exstring5():
    "exercicios" in "fizeram os exercicios?"
    
    "ícios" in "Fizeram a exercícios?"

    "Abril" in "Fizeram os exercícios?"

def exstring6():
    numeros = "1; 2 ;3"
    listanumeros = list(numeros)
    print(listanumeros)

def exstring7():
    l = list("atividade")
    print(",".join(l))

def exstring8():
    str = "Atividade"
    print(str.lower())
    print(str.upper())
    
def exerciciostring():
    # Faça um programa que conta o número de palavras de um texto
    str = input("Digite uma frase: ")
    palavras = str.split()
    print(f"A Frase '{str}' contém {len(palavras)} palavras")

exerciciostring()
