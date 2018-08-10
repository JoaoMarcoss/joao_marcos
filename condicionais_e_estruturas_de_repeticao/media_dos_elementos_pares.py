lista = input().split()
soma = 0
cont = 0
media = 0
i = 0

for i in range(len(lista)):
    if (int(lista[i]) > 0) and (int(lista[i]) % 2 == 0):
        soma = soma + int(lista[i])
        cont = cont + 1
        i = i +1
if (soma != 0):
    media = soma / cont
    print("%.2f" %media)
else:
    print("-1")
    
