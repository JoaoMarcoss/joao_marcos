peso = int(input())
maximo = 560
cont = 0
soma = 0

while ((peso != 0) and (cont < 7)) and (soma < maximo):
    soma = soma + peso
    cont = cont + 1
    peso = int(input())

print(cont)
print("%.1f" %soma)
