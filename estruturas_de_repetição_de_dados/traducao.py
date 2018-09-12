n, m = 0, 1
while n != m and m != 0:
    n, m = map(int, input().split(' '))
    if n == m and m == 0:
        break
    regras = []
    text = []
    for x in range(n):
        result = input()
        regras.append(result.split(' -> '))
    for x in range(m):
        result = input()
        text.append(result)
    verificar = []
    for x in range(len(text)):
        for i in range(len(regras)):
            result = text[x].replace(regras[i][0], regras[i][1])
            text[x] = result
    for x in text:
        print(x)
