def selection_sorted(lista):
    n = len(lista)
    for i in range(n - 1):
        index = i
        for j in range (i, n):
            if lista[j] < lista[index]:
                index = j
        if lista[i] > lista[index]:
            aux = lista[i]
            lista[i] = lista[index]
            lista[index] = aux
    return lista
def selection_sorted2(lista):
    n = len(lista)
    for i in range(n - 1):
        index = i
        for j in range(i, n):
            if lista[j] < lista[index]:
                index = j
        if lista[i] > lista[index]:
            aux = lista[i]
            lista[i] = lista[index]
            lista[index] = aux
    return lista

lista = list(map(int, input().split()))

res = selection_sorted2(lista)
print(res)
