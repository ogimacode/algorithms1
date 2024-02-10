#laços para ler e escrever a lista
lista = []

i = 0
while i < 10:
    x = int(input())
    lista.append(x)
    i += 1

j = 0
while j < 10:
    print(lista[j], end=' ')
    j += 1
