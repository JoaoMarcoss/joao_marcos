def binario(n, bin):
    if n == 0:
        return bin
    bin.append(n % 2)
    if n != 0:
        return binario(n // 2, bin)
lista = []
n = int(input())
if n == 0:
    print(n)
else:
    numero_binario = binario(n, lista)
    for x in range(len(numero_binario) - 1, -1, -1):

print(numero_binario[x])
