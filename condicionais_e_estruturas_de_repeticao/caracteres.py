n = int(input())
while(n <= 100000) and (n != 0):
    palavra = str(input())
    if (len(palavra) == 1):
            print(palavra)
            n = int(input())
    if (n == 0):
        break
    elif len(palavra) > 1:
        palavra = (palavra[::-1])
        print(palavra)
        n = int(input())
