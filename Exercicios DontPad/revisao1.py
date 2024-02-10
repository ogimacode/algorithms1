def faz_lista(lista1,lista2):
    lista3 = []
    for elem in lista1:
        lista3.append(elem)
    for elem in lista2:
        lista3.append(elem)
    n = len(lista3)
    for i in range(n - 1):
        index = i
        for j in range(i, n):
            if lista3[j] < lista3[index]:
                index = j
        if lista3[i] > lista3[index]:
            aux = lista3[i]
            lista3[i] = lista3[index]
            lista3[index] = aux 
    return lista3
lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

res = faz_lista(lista1, lista2)
print(res)