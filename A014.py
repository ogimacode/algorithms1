num = int(input())

uni = num % 10
dez = (num //10) % 10
cen = (num //100) % 10
mil = num // 1000

numero_invertido = mil + cen*10 + dez*100 + uni*1000

print(numero_invertido)