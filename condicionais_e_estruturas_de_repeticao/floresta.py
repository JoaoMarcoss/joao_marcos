arvores = int(input())
combinacao = 5
passo = 3
base = 1
cont = 0

while ((base*base) <= (arvores/2)):
    if((arvores - combinacao)% passo == 0):
        cont = cont + 1
    combinacao = combinacao + 3
    passo = passo + 2
    base = base + 1
print(cont)   
