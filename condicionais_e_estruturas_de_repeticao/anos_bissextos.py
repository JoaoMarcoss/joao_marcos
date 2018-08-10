anos = input().split()
cont = int(anos[0])
fim = int(anos[1])
result = []

while cont <= fim:
    if ((cont % 4 == 0) and (cont % 100 != 0) or (cont % 400 == 0)):
        result.extend([cont])
        cont = cont + 1
    else:
        cont = cont + 1
if (result == []):
    print("-1\n")
if (result != 0):
    print(*result, sep = "\n")
    
    
        
    
    
