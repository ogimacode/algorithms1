def remover_consecutivos(lista):
    lista_sem_repeticao = []
    n = len(lista)
    for i in range(n):
        if lista[i] != lista[i - 1]:
            lista_sem_repeticao.append(lista[i])
    return lista_sem_repeticao


lista = list(map(str, input().split()))

res = remover_consecutivos(lista)
print(res)