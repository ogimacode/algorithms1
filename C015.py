n = int(input())
i = 2

while i <= n:
    if n % i != 0:
      i = i + 1
    else:
        if n > i:
            print(0)
            break
        else:
            print(1)
            break

if n <= 1:
  print(0)