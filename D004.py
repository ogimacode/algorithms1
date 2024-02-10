n = int(input())

lista = list(map(int,input().split()))

x = int(input())

indice = -1
i = 0
while i < len(lista):
    if lista[i] == x:
        indice = i
        i = len(lista)
    i += 1

if indice <= len(lista):
    print(indice)
else:
    print(-1)