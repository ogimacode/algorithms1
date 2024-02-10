p1 = input()
p2 = input()

i = 0
while i < len(p1):
    j = 0
    igual = False
    while j < len(p2) and not igual:
        if p1[i] == p2[j]:
            igual = True
        j += 1
    if igual == False:
        break
    i += 1

if igual == False or len(p1) != len(p2):
    print(0)
else:
    print(1)


