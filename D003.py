num = int(input())
val = input().split()

maior = 0
i = 0
position = 0
while i < num:
    if int(val[i]) > maior:
        maior = int(val[i])
        position = i
    i += 1

print(maior)
print(position)
