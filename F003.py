dimencao_matriz = input().split()
num_linhas = dimencao_matriz[0]
num_colunas = dimencao_matriz[1]
numeros = input().split()
posicao = 0
matriz = []

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
for i in range(len(dimencao_matriz)):
    dimencao_matriz[i] = int(dimencao_matriz[i])

num_linhas = dimencao_matriz[0]
num_colunas = dimencao_matriz[1]    

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        linha.append(numeros[posicao])
        posicao += 1
    matriz.append(linha)

for i in range(num_colunas):
    soma = 0
    for j in range(num_linhas):
        soma += matriz[j][i]
    print(soma)