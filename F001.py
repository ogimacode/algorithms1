n = input().split()
linhas= int(n[0])
colunas= int(n[1])
numeros= input().split()

aux = colunas
mat = []

j = 0
for i in range(linhas):
    linha = []

    while j < colunas:
        linha.append(numeros[j])
        j += 1
    mat.append(linha)
    colunas = colunas + aux

colunas = aux

for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j], end=" ")
    print()