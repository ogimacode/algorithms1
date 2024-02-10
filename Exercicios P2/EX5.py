def cria_matriz(linha, coluna):
    matriz = []
    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            x = 0
            matriz[i].append(x)
    return matriz

def imprime_matriz(matriz):
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end=' ')
        print()
    

linha = int(input())
coluna = int(input())

matriz = cria_matriz(linha, coluna)

imprime_matriz(matriz)