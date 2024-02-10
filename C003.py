x = int(input())
y = int(input())

i = x
j = y
if x > y:
  print('INVALIDO')
else:
  while i <= y:
    print(i)
    i = i + 1
    
while j >= x:
  print(j)
  j = j - 1