n = int(input())
maior1 = 0
maior2 = 0
i = 0
while i < n :
    num = int(input())
    if num >= maior1 or i < 1:
        maior2 = maior1
        maior1 = num
    elif num > maior2:
        maior2 = num
    i += 1
print(maior1)
print(maior2)