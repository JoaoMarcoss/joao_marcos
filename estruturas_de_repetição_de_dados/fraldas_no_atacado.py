def quantidade(idade):
    if (idade <= 2):
        return 9
    else:
        return 6
    
idade = 0
fraldas_dia = []

while True:
    idade = int(input())
    continua = input().lower()
    fraldas_dia.append(quantidade(idade))
    if (continua == 'não'):
        break

result = (sum(fraldas_dia)) * 30
n = 0

while (n * 100 < result):
    if (n * 100 < result):
        n += 1
    if (n * 100 >= result):
        break

print(n)
print(n * 100 - result)
