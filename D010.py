n = int(input())

lista = list(map(int, input().split()))

i = 0
par = []
impar = []
while i < n:
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
    i += 1
i = 0
while i < len(par):
    print(par[i], end=' ')
    i += 1
i = 0
print()
while i < len(impar):
    print(impar[i], end=' ')
    i += 1
print()