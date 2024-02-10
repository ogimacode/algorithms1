#                0  1  2  3  4  5  6
lista_exemplo = [5, 2, 8, 9, 3, 1, 7]

indice_remover = 2

i = indice_remover
while i < len(lista_exemplo) - 1:
    lista_exemplo[i] = lista_exemplo[i + 1]
    i += 1
lista_exemplo.pop()
print(lista_exemplo)

# Algortmo com input

lista = list(map(int, input(f'Digite a lista: ').split()))

remover = int(input(f'Digite o indice que será removido: '))

i = remover
while i < len(lista) - 1:
    lista[i] = lista[i + 1]
    i += 1
lista.pop()

print(lista)
