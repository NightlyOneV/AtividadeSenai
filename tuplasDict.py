def extupla1():
    t1 = 'a', 
    t2 = ('a')
    print(type(t1))
    print(type(t2))
    
def extupla2():
    # Erro proposital de TUPLA não imutavel!
    
    a = (24, "Abril", 9.5, 1)
    a[2] = 9.0
    
def extupla3():
    a = (24, "Abril", 9.5, 1)
    print(a[2])
    print(a[1:3])

def extupla4():
    x,y = (18,20)
    print(x)
    print(y)
    print(x + y)

def exdict1():
    ra = {"Liz": 229874,
          "Hugo": 215794,
          "Sofia": 199745
          }
    print(type(ra))
    print(ra["Liz"])
    print(ra)
    
    ra["Hugo"] = 215799
    ra["Diego"] = 959532
    print(ra)
    
    for x in ra:
        print(x)
        
    print(ra.items())
    print(ra.keys())
    print(ra.values())
    
    print(ra.get("Hugo"))
    
    for nome,numero in ra.items():
        print(nome, numero)
    
exdict1()