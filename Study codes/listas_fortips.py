#Utilizando o for com contagem nos elementos da lista. Tem o problema de sempre checar todos os números. Pode ser revertido o problema com o uso do break
def buscar_v1(lista, x):
    achou = False
    for elem in lista:
        if x == elem:
            achou = True
    return achou

#Utilizando o for com elementos, mas adicionando o break
def buscar_v2(lista, x):
    achou = False
    for elem in lista:
        if x == elem:
            achou = True
            break
    return achou

#Utilizando o while com contagem no indice da lista, algortmo clássico, busca sequencial
def buscar_v3(lista, x):
    i = 0
    achou = False
    while i < len(lista) and not achou:
        if lista[i] == x:
            achou = True
        i += 1
    return achou
lista = [1, 2, 3, 4, 5, 6]
x = int(input())

#Selecione a versão do buscar
if buscar_v3(lista, x):
    print('achou')
else:
    print('não achou')