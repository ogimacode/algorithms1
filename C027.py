n = int(input())

i = 1
acu = 0
while i < n:
    if n % i ==0:
        acu = acu + i

    i = i + 1
if acu == n:
    print(f'S')
else:
    print(f'N')