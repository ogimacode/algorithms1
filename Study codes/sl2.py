n = int(input())

list = []
maior = 0
i = 0
s = 0
while i < n:
    altura = float(input())
    list.append(altura)
    if altura > maior:
        maior = altura
        s += 1
    i += 1
j = 0
while j < n:
    print(list[j], end=' ')
    j += 1
print(f'\n {maior}')

