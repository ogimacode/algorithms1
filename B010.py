l1 = int(input())
l2 = int(input())
l3 = int(input())


if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('INVALIDO')
elif l1 == l2 == l3:
    print('EQUILATERO')
elif l1 != l2 != l3 != l1:
    print('ESCALENO')
else:
    print('ISOSCELES')