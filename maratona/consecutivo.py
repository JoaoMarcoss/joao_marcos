n = int(input())
valor = input()
valores = list(map(int,valor.split(' ')))
tamanho = len(valores)
atual = 0
maior = 0

for i in range(0,tamanho-1,1):
    if(valores[i] == valores[i+1]):
        atual += 1
    if(valores[i] != valores[i+1]):
        if(atual > maior):
            maior = atual
        atual = 0
    if(atual > maior):
            maior = atual
maior = maior + 1
print(maior)
