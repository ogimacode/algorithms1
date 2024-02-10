ana = int(input())

nana = 0
i = 0
n1 = 1
n2=  2
n3 = 3
while i < ana:
    nana = n1 * n2 * n3
    if nana == ana:
        print(f'S')
        break
    if nana > ana:
        print(f'N')
        break
    n1 = n1 + 1
    n2 = n2 + 1
    n3 = n3 + 1
    i = i + 1