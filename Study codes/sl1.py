list = []

i = 0
soma = 0
while i < 10:
    num = float(input())
    list.append(num)
    soma += num
    i += 1
j = 0
while j < 10:
    print(list[j], end=' ')
    j += 1
k = 0
print()
while k < 10:
    if list[k] % 2 == 0:
        print(list[k], end=' ')
    k += 1
print(f'\n{soma}')