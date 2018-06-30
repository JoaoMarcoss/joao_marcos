v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0
v10 = 0
v11 = 0
v12 = 0
valor = float(input())
if(valor//100>0):
    v1 = valor//100
    valor = valor - (v1 * 100) 
if(valor//50>0):
    v2 = valor//50
    valor = valor - (v2 * 50)
if(valor//20>0):
    v3 = valor//20
    valor = valor - (v3 * 20) 
if(valor//10>0):
    v4 = valor//10
    valor = valor - (v4 * 10)
if(valor//5>0):
    v5 = valor//5
    valor = valor - (v5 * 5) 
if(valor//2>0):
    v6 = valor//2
    valor = valor - (v6 * 2)
if(valor//1>0):
    v7 = valor//1
    valor = valor - (v7 * 1.00)
if(valor < 1 and (valor*100)//50>0):
    v8 = (valor*100)//50
    valor = valor - (v8 * 0.50)
if(valor < 1 and (valor*100) // 25>0):
    v9 = (valor*100)//25
    valor = valor - (v9 * 0.25) 
if(valor < 1 and (valor*100) // 10>0):
    v10 = (valor*100)//10
    valor = valor - (v10 * 0.10)
if(valor < 1 and (valor*100) // 5>0):
    v11 = (valor*100)//5
    valor = valor - (v11 * 0.05)
if(valor < 1 and (valor*100) // 1>0):
    v12 = (valor*100)//1
    valor = valor - (v12 * 0.01) 
        
print("NOTAS:")
print("%i nota(s) de R$ 100.00"%v1)
print("%i nota(s) de R$ 50.00"%v2)
print("%i nota(s) de R$ 20.00"%v3)
print("%i nota(s) de R$ 10.00"%v4)
print("%i nota(s) de R$ 5.00"%v5)
print("%i nota(s) de R$ 2.00"%v6)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00"%v7)
print("%i moeda(s) de R$ 0.50"%v8)
print("%i moeda(s) de R$ 0.25"%v9)
print("%i moeda(s) de R$ 0.10"%v10)
print("%i moeda(s) de R$ 0.05"%v11)
print("%i moeda(s) de R$ 0.01"%v12)
