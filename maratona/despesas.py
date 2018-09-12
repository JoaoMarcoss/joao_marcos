clara = 0
diana = 0
i = 0
total = 0

while (i <= 5):
    valor = float(input())
    nome = input()
    if (nome == "Clara"):
        clara = clara + valor
    else:
        diana = diana + valor
    total = total + valor
    i = i + 1

if (clara == diana):
    print("MORADORAS QUITES")
elif (clara < diana):
    print("CLARA\n%.2f" % ((total / 2) - clara))
else:
    print("DIANA\n%.2f" % ((total / 2) - diana))
