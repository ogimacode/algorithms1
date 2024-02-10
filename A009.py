a= float(input())
b= float(input())
c= float(input())

delta = (b**2) - 4*a*c
x1 = (-b + pow(delta,0.5))/(2*a)
x2 = (-b - pow(delta,0.5))/(2*a)

print(f'{x1:.2f}')
print(f'{x2:.2f}')