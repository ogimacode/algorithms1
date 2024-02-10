# Ordenamento por seleção
lista = [3, 6, 2, 7, 8, 5, 9, 10, 1, 4]



def selection_sorted(lista):
    for i in range(len(lista) - 1):
        min_index = i
        for j in range(i, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        if lista[i] > lista[min_index]:
            aux = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = aux
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

res = selection_sorted2(lista)
print(res)
