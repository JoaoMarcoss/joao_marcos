Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def algoritmo_de_euclides(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 % n2 == 0:
        return n2
    return algoritmo_de_euclides(n1, n2 % n1)

quantidade = int(input())

for x in range(quantidade):
    n1, n2 = map(int, input().split())
print("MDC(%d,%d) = %d" % (n1, n2, algoritmo_de_euclides(n1, n2)))
