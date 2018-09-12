Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sequencia_pares(n, result):
    if result == n - 1:
        return result
    if result % 2 == 0:
        print(result)
        if result < n - 2:
            return sequencia_pares(n, result + 2)
        elif result == n - 2:
            return n

n = int(input())
print(sequencia_pares(n, 0))
