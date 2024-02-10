def buscar(x, lista):
    for elem in lista:
        if x == elem:
            return True
    return False

def lista_sem_repeticao(lista):
    lista_nova = []
    for elem in lista:
        if not buscar(elem, lista_nova):
            lista_nova.append(elem)
    return lista_nova



l1 = list(map(int,input().split()))
l2 = lista_sem_repeticao(l1)

print(l2)