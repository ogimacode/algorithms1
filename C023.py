idade = int(input())
altura = int(input())
maior = altura
velas = 1
i = 1
while i < idade:
    altura = int(input())
    if altura > maior:
        velas = 1
        maior = altura
    elif maior == altura:
        velas += 1
    i += 1    
print(velas)