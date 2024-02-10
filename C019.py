base = int(input())
expo = int(input())


pot1 = 0
pot2 = base
i = 1
j = 0

while i < expo:
    while j < pot2:
        pot1 = pot1 + base
        j = j + 1
    base = pot1
    pot1 = 0
    j = 0
    i = i + 1

if expo == 0:
    print(1)
else:
    print(base)