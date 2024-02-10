idade = int(input())

if idade >= 70 or idade <= 15:
  print('DISPENSADO')
elif idade >= 18:
  print('OBRIGATORIO')
else:
  print('FACULTATIVO')