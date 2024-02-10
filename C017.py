n = int(input())

fatzero = 1
fat = 1
acu = 0
i = 1
while i <= n:
    fat = fat * i
    acu = acu + fat
    i = i + 1

acu = acu + fatzero
print(acu)