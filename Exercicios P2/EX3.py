# Faça uma função que receba por parâmetro uma lista, um índice e um elemento. A função deve inserir o elemento no índice indicado. 
# A função deve retornar True se inseriu o elemento e False caso contrário.
def inserir_elemento(lista, indice, elemento):
    achou = False
    lista.append(-1)
    i = len(lista) - 2
    while i >= indice:
        lista[i + 1] = lista[i]
        if i == indice:
            lista[i] = elemento
            achou = True
        i -= 1
    if achou == False:
        lista.pop()
    return achou


lista = list(map(int,input(f'Digite a lista: ').split()))

indice = int(input(f'Digite o indice: '))

elemento = int(input(f'Digite o elemento: '))

if inserir_elemento(lista, indice, elemento):
    print(f'True')
else:
    print(f'False')
print(lista)