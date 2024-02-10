#        0  1  2  3  4  5  6
# Adicionando números em uma lista
lista_exemplo = [5, 2, 8, 9, 3, 1, 7]

x = 100
indice_inserir = 2

lista_exemplo.append(-1)

i = len(lista_exemplo) - 2
while i >= indice_inserir:
    lista_exemplo[i + 1] = lista_exemplo[i]
    i -= 1

lista_exemplo[indice_inserir] = x

print(lista_exemplo)


# Inserir na lista feito com input

lista = list(map(int, input(f'Digite a lista: ').split()))

num = int(input(f'Digite o número a ser inserido: '))
inserir = int(input(f'Digite em qual indice é para o número ser inserido: '))

lista.append(-1)
i = len(lista) - 2
while i >= inserir:
    lista[i + 1] = lista[i]
    i -= 1
lista[inserir] = num 
print(lista)