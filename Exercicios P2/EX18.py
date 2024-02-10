def buscar(lista, x):
    achou = False
    for elem in lista:
        if elem == x:
            achou = True
            break
    return achou




lista = list(map(int,input().split()))
x = int(input())

if buscar(lista, x):
    print('Achou')
else:
    print('Não achou')