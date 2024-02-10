n = int(input())

lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

i = 0
lista3 = []
while i < n:
    val = lista1[i] + lista2[i]
    lista3.append(val)
    print(lista3[i], end=' ')
    i += 1