lar = float(input())
alt = float(input())
valor = float(input())
rendi = float(input())

area = lar * alt
latas = area / rendi
arredon = round(latas + 0.5)
total = arredon * valor

print(arredon)
print(f'{total:.2f}')