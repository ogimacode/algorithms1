linhas = 3
colunas = 4
mat = []

for i in range(linhas): #como ler matrizes 
    mat.append([])
    for j in range(colunas):
        x = int(input(f"Informe o numero [{i}][{j}]: "))
        mat[i].append(x);

for i in range(linhas): #como escrever matrizes
    for j in range(colunas):
        print(mat[i][j], end=' ')
    print()
