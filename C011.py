x = int(input())

i = 1
j = 1
quanti = 0
while j > -1:
  j = int(input())
  i = i + 1
  if x == j:
    quanti = quanti + 1
print(quanti)