n = int(input())

palin = 0
i = n
while i != 0:
    palin = palin * 10
    palin = palin + i % 10
    i = i // 10
if palin == n:
    print(f'S')
else:
    print(f'N')