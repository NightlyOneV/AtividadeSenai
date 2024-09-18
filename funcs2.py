""" 


adsadsadsadsadsa

"""

def reverso(num=0):
    nnumb = str(num)
    return int(nnumb[::-1])
    
def quantidade(num):
    qntd = len(str(num))
    print(qntd)
    
def expo(num,num2):
    resultado = 1 
    if (num > 0 and num2 > 0):
        for _ in range(num2):
            resultado *= num
        return resultado
    else: 
        return "Invalido"
    
def ex1():
    def f1(a):
        print(a+x)
    
    def f2(a):
        c = 10
        print(a+x+c)
        
    def f3(a):
        global x 
        x = x + 1
        print(a+x)
    
    def f4(a):
        a.append(3)
        
    
    til = [1,2]
    f4(til)
    print(til)

    f1(3)
    f3(3)
    print(x)
    
    
x = 4 
    
ex1()