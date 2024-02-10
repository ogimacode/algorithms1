linhas = int(input())
colunas = int(input())
mat = []

for i in range(linhas):
    mat.append([])
    for j in range(colunas):
        x = int(input(f"Informe o numero [{i}][{j}]: "))
        mat[i].append(x);

for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j], end=' ')
    print()