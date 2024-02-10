def lista_prima(lista):
    i = 0
    while i < len(lista):
        j = 2
        while j < len(lista):
            if lista[i] % j != 0:
                primo = True
                j += 1







lista = list(map(int, input().split()))
