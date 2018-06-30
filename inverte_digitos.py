n = input()
l = n
k = len(str(n))
n = int(n)
d = len(str(n))
cont = 0
invertido = 0
v = 0
diff = 0
while (d >= 1):
    d = d - 1
    pow = 10**d
    v = (int(n/pow))
    invertido = invertido + v*(10**cont)
    n = n%pow
    cont = cont + 1
r = int(invertido)
invertido = len(str(invertido))
p = 0
p = str(p)
print(invertido)
print(k)
if (invertido < k) and (cont == 1):
    diff = k - invertido
    u = str(diff)
    r = str(r)
    invertido = r + (p * diff)
    print(invertido)
elif (invertido < k):
    diff = k - invertido
    u = str(diff)
    r = str(r)
    invertido = (p * diff) + r
    print(invertido)
else:
    print (invertido)
