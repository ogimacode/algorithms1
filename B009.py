a = int(input())
b = int(input())
c = int(input())

if a > b and b > c:
    au = a
    a = c
    c = au
elif c > a and a > b:
    au = a
    a = b
    b = au
elif b > c and c > a:
    au = b
    b = c
    c = au
elif b > a and a > c:
    au = a
    a = c
    c = b
    b = au
elif a > c and c > b:
    au = a
    a = b
    b = c
    c = au
elif a == c and b > a:
    au = b
    b = c
    c = au
elif a == c and b < a:
    au = a
    a = b 
    b = c 
    c = au 
elif b == c and a > b:
    au = a 
    a = c 
    c = au

print(a)
print(b)
print(c)