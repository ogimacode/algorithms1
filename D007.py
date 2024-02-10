n = int(input())

lista = list(map(int, input().split()))

i = 0
while i + 1 < n:
    aux = lista[i]
    lista[i] = lista[i + 1]
    lista[i + 1] = aux
    i += 2

i = 0 
while i < n:
    print(lista[i], end=" ")
    i += 1