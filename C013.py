n = int(input())

i = 0
soma = 0
while i < n:
    num = int(input())
    soma += num
    if i == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    i += 1

print(maior)
print(menor)
print(soma)
