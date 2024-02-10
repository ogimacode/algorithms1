a = int(input())
b = int(input())

while b != 0:
  resto = a % b
  a = b
  b = resto
  if b == 0:
    print(a)