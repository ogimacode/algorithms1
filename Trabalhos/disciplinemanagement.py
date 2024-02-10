alunos = int(input(f'Informe a quantidade de alunos: '))
trabalho = int(input(f'Informe a quantidade de trabalhos: '))

i = 0
somaprovas = 0
mf = 0
reprovado = 0
recuperando = 0
aprovado = 0
mfsoma = 0
while i < alunos:
    p1 = float(input(f'Informe a nota da P1: '))
    p2 = float(input(f'Informe a nota da P2: '))
    ps = float(input(f'Informe a nota da PS: '))
    if ps > 0:
        if p1 < p2:
            p1 = ps
        elif p2 < p1:
            p2 = ps
    somaprovas = p1 + p2
    j = 0
    somatrab = 0
    while j < trabalho:
        trab = float(input(f'Informe a nota do trabalho {j + 1}: '))
        somatrab += trab
        j += 1
    mf = (somatrab / trabalho) * 0.4 + (somaprovas / 2) * 0.6
    mfsoma += mf
    if mf < 4:
        print(f'Nota do Aluno {i + 1}: {mf:.2f} Reprovado')
        reprovado += 1
    elif mf >= 4 and mf < 6:
        print(f'Nota do Aluno {i + 1}: {mf:.2f} Recuperação')
        recuperando += 1
    else:
        print(f'Nota do Aluno {i + 1}: {mf:.2f} Aprovado')
        aprovado += 1
    i += 1
mfsala = mfsoma / alunos
print(f'Alunos aprovados: {aprovado}')
print(f'Alunos em recuperação: {recuperando}')
print(f'Alunos reprovados: {reprovado}')
print(f'Média da sala: {mfsala:.2f}')