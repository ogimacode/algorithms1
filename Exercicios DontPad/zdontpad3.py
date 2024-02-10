def produto_escalar(lista1, lista2):
    total = 0
    for i in range(len(lista1)):
        mult = lista1[i] * lista2[i]
        total += mult
    return total

lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

res = produto_escalar(lista1, lista2)
print(res)