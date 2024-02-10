# Faça uma função que receba por parâmetro uma lista e um índice. A função deve remover elemento do índice indicado. 
# A função deve retornar True se removeu o elemento e False se não removeu.
def remove_elemento(lista, indice):
    i = indice
    achou = False
    while i < len(lista) - 1:
        lista[i] = lista[i + 1]
        if indice == i:
            achou = True
        i += 1
    if achou == True:
        lista.pop()
    return achou



lista = list(map(int, input(f'Digite a lista: ').split()))
indice = int(input(f'Digite o indice do elemento a ser removido: '))

if remove_elemento(lista, indice):
    print(f'True')
else:
    print('False')
print(lista)