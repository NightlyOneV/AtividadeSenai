x = [1,2,3,4,5]
y = [2,7,8,9,10]

encontrado = False

for i in range(len(x)):
    if y.count(x[i]) > 0:
        print(f"Foi encontrado o número '{x[i]}' | {y.count(x[i])} veze(s)") 
        encontrado = True 
        
        
if encontrado == False:
    print("Não foi encontrado nenhum número repetido na lista.")