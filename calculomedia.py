def reverso(num=0):
    nnumb = str(num)
    return int(nnumb[::-1])
    
def quantidade(num):
    qntd = len(str(num))
    print(qntd)
    
print(quantidade(150))