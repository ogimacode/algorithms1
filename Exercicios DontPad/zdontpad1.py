def inserir_elemento(lista):
    for elem in lista:
        if elem == x:
            return "Não pode ser repetido"
    lista.append(-1)
    lista[len(lista) - 1] = x
    return lista

lista = list(map(int, input().split()))
x = int(input())

res = inserir_elemento(lista)
print(res)