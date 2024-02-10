n = int(input())

h = 0 #acumulador
i = 1 #contador
while i <= n:
    h =  h + 1 / i
    i = i + 1
print(f'{h:.4f}')

