numero = int(input())
arrayfinal = []

array = input()
array = array.split(' ')
array = list(map(int, array))

for i in range(len(array)-1, -1, -1):
    arrayfinal.append(array[i])

print(*arrayfinal)

trocafinal = len(array)
array.insert(trocafinal, array[0])
del(array[0])
arrayfinal = array
print(*arrayfinal)

array.sort(reverse = True)
arrayfinal = array
print(*arrayfinal)
