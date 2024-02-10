x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())
encontro = "NAO"
if (x1 > x2 and v2 > v1) or (x2 > x1 and v1 > v2):
    t = (x1 - x2) / (v2 - v1)
    if t >= 0 and t % 1 == 0:
        encontro = "SIM"
print(encontro)