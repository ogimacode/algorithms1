par = 0 #dois acumuladores 'par,impar'
impar = 0
i = 1   # um contador
while i != 0:
    i = int(input())
    if i != 0:
        if i % 2 == 0:
            par = par + i
        else:
            impar = impar + i
total = par + impar       
print(par)
print(impar)
print(total)

