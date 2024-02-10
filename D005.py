n = int(input())
val = list(map(int,input().split()))

x = int(input())
i = 0
soma = 0
while i < n:
    if x == val[i]:
        soma += 1
    i += 1
print(soma)