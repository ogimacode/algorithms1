def lista_crescente(lista):
    crescente = True
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            crescente = False
            break
        i += 1
    return crescente

lista = list(map(int, input().split()))

if lista_crescente(lista):
    print('True')
else:
    print('False')