n = int(input())

lista = list(map(int, input().split()))

indice = n - 1
i = 0
while i < n:
  print(lista[indice - i], end=' ')
  i += 1