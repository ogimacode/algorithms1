qtd_alunos = int(input('informe a qtd de alunos:'))
qtd_provas = int(input('informe a qtd de provas:'))

soma_media_sala = 0
i = 0
while i < qtd_alunos:
    nome = input('Nome do aluno:')
    soma_notas_aluno = 0
    j = 0
    while j < qtd_provas:
        nota = float(input(f'informe a nota {j+1}:'))
        soma_notas_aluno = soma_notas_aluno + nota
        j = j + 1
    media_aluno = soma_notas_aluno / qtd_provas
    soma_media_sala = soma_media_sala + media_aluno
    print(f'A media de {nome} é {media_aluno}')
    i = i + 1
media_sala = soma_media_sala / qtd_alunos
print(f'A media da sala é {media_sala}')
