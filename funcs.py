def leNumeroInt():
    numero = input("digite um numero inteiro: ")

    return int(numero)

r = leNumeroInt()
print("numero digitado é :" , r)

def soma (numero1 ,numero2):
    resultado = numero1 + numero2

    return resultado 

n1 = leNumeroInt()
n2 = leNumeroInt()
res  = soma (n1 , n2)
print ("a soma é :" , res)

def imprimirCaixa(num):
    Tam = len(str(num))
    for i in range(12+Tam):
        print("+", end='')
        
    print()
    print("| Número: ", num, "|")
    for i in range(12+ Tam):
        print("+", end="")

    print()
    
imprimirCaixa(10)
    