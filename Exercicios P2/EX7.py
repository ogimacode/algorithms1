def lista_igual(l1, l2):
    igual = True
    for i in range(len(l1)):
        if len(l1) != len(l2):
            igual = False
        if l1[i] != l2[i]:
            igual = False
    return igual

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

if lista_igual(l1, l2):
    print('True')
else:
    print('False')