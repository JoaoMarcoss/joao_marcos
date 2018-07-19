n = int(input())
i = 1
t = 0
while t < n:
        t = i*(i+1)*(i+2)
        i = i+1
if t == 0:
    print ("Falso")
elif t == n:
    print ((i-1), "*", (i), ("*"), (i+1), ("="), t)
    print ("Verdadeiro")
elif t < 0:
    print ("Falso")
else:
    print ("Falso")
