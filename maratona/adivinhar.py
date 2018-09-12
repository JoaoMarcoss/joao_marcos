acaba = False
partidas = int(input())
j = 0

while(j < partidas):
    while(acaba == False):
        senha = 0
        chute = 0
        quantidade = int(input())
        i = 0
        senha = input()
        while(i < quantidade):
            chute = input()
            result = 0
            excelente = 0
            bom = 0
            while(result < len(senha)):
                if(senha[result] == chute[result]):
                    excelente = excelente + 1
                else:
                    result2 = 0
                    while(result2 < len(senha)):
                        if(chute[result2] == senha[result]):
                            bom = bom + 1
                            break
                        result2 = result2 + 1
                result = result + 1
            print("(%i,%i)"%(excelente,bom))
            if(excelente == len(senha)):
                acaba = True
            i = i + 1
    acaba = False
j = j + 1
