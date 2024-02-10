def inserir_elemento(lista):
    for i in range(len(lista)):
        if x < lista[i]:
            guardar_index = i
            break
    lista.append(-1)
    j = len(lista) - 2
    while j >= guardar_index:
        lista[j + 1] = lista[j]
        j -= 1
    lista[guardar_index] = x
    return lista


lista = list(map(int, input().split()))
x = int(input())

res = inserir_elemento(lista)
print(res)