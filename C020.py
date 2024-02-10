idade = 1
i = -1
soma_idade = 0
maiores = 0
velhos = 0
while idade >= 0:
    idade = int(input())
    if idade  > 0:
        soma_idade = soma_idade + idade
    if idade >= 18:
        maiores = maiores + 1
    if idade > 75:
        velhos = velhos + 1
    i = i + 1
media = soma_idade / i
velhos = velhos / i * 100
print(f'{media:.2f}')
print(maiores)
print(f'{velhos:.2f}%')