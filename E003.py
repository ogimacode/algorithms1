palavra = input()

caracter = input()

i = 0
cont = 0
while i < len(palavra):
    if palavra[i] == caracter:
        cont += 1
    i += 1

print(cont)