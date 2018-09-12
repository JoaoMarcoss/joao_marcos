def regeneracao_de_vida(dic, atk, reg):
    hp_init = 100
    tempo = 0
    dano = 0
    result = 0
    for x in range(atk + 1):
        dano = dic[x][0]
        tempo = dic[x][1] - result
        result = tempo
        hp_init -= dano
        if hp_init <= 0:
            return True
        hp_init += tempo * reg
    return False

x = int(input())
resultados = {}
hp = 100
d = t = 0
result = []

for x in range(x):
    d, t = map(int, input().split(' '))
    result.append(d)
    result.append(t)
    resultados[x] = result
    result = []
y = int(input())
hp_final = regeneracao_de_vida(resultados, x, y)

if hp_final == False:
    print('Inimigo Vivo')
else:
    print('Inimigo Morto')
