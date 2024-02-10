# Faça uma função que receba por parâmetro uma lista e um elemento e retorna a primeira posição que o elemento se encontra. 
# Se não for encontrado, retornar -1.
def encontra_elem(lista, elem):
    i = 0
    posicao = None
    while i < len(lista):
        if elem == lista[i]:
            posicao = i
        i += 1
    return posicao

lista = list(map(int, input(f'Digite a lista: ').split()))
elem = int(input(f'Digite o valor a ser encontrado o indice: '))

res = encontra_elem(lista, elem)

print(res)