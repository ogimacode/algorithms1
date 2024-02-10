xqui = float(input())
valor1 = float(input())
valor2 = float(input())
viagem = float(input())

if viagem > xqui:
  total = viagem * valor2
else:
  total = viagem * valor1

print(f'{total:.2f}')
