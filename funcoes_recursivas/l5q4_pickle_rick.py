def fibonacci(n):
  if (n <= 1):
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
antidoto = fibonacci(n)

if (antidoto == 0):
  print("O antidoto nao e necessario")
elif (antidoto > 0):
  print("%d mg/L" % (antidoto))
