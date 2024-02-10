def cria_matriz(quadrada):
    matriz = []
    for i in range(quadrada):
        matriz.append([])
        for j in range(quadrada):
            if j == i:
                matriz[i].append(1)
            else:
                matriz[i].append(0)
    return matriz

def imprime_matriz(matriz):
    for i in range(quadrada):
        for j in range(quadrada):
            print(matriz[i][j], end=' ')
        print()

quadrada = int(input())

matriz = cria_matriz(quadrada)

imprime_matriz(matriz)