def selecao_de_nomes(lista, busca):
    nomes_encontrados = []
    for x in lista:
        if busca in x.lower():
            nomes_encontrados.append(x)
    return nomes_encontrados

nomes = []
nome = ''

for x in range(10):
    nome = input()
    nomes.append(nome)
buscar = input().lower()
result_pesquisa = selecao_de_nomes(nomes, buscar)

for x in result_pesquisa:
    print(x)
