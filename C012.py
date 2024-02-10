n = int(input())

i = 0
while i < n:
    num = int(input())
    if i == 0:
        maior = num
    if num > maior:
        maior = num
    i += 1

print(maior)