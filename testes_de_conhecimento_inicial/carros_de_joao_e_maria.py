digita = input()
ano = 0
anoaux = 0
velocidade = 0
velocidadeaux = 0
media = 0
cont = 0
result = 0
while (digita == 's'):
    ano = int(input())
    velocidade = float(input())
    if (ano > anoaux):
        anoaux = ano
    media = media + velocidade
    if (velocidade > velocidadeaux):
        velocidadeaux = velocidade
    cont = cont +1
    digita = input()        
if ((digita == 'n') and (cont != 0)):
    result = media / cont
    print ("{:.2f}".format(velocidadeaux))
    print (anoaux)
    print ("{:.2f}".format(result))
elif (digita == 'n'):
    print("zero") 
