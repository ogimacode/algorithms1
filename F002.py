dimencao_matriz = input().split()
numeros = input().split()
posicao = 0
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
for i in range(len(dimencao_matriz)):
    dimencao_matriz[i] = int(dimencao_matriz[i])    
matriz = []
for i in range(dimencao_matriz[0]):
    linha = []
    for j in range(dimencao_matriz[1]):
        linha.append(numeros[posicao])
        posicao += 1
    matriz.append(linha)
#soma
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
    print(soma)