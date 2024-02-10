def buscar_v1(lista, x):
    achou = False
    for elem in lista:
        if x == elem:
            achou = True
    return achou

def buscar_v2(lista, x):
    achou = False
    i = 0
    while i < len(lista) and not achou:
        if lista[i] == x:
            achou = True
        i = i + 1
    return achou

def buscar_v3(lista, x):
    achou = False
    for elem in lista:
        if x == elem:
            achou = True
            break
    return achou


def buscar_v4(lista, x):
    for elem in lista:
        if x == elem:
            return True
    return False
    


lista = [7, 3, 5, 8]
x = 10

if buscar_v4(lista, x):
    print("achou!")
else:
    print("nao achou!")

