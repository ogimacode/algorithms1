palavra = input()

i = 0
j = len(palavra) - 1
while i < len(palavra):
    if palavra[i] == ' ':
        i += 1
    if palavra[j] == ' ':
        j -= 1
    if palavra[i] == palavra[j]:
        igual = True
    else:
        igual = False
        break
    i += 1
    j -= 1

if igual:
    print(1)
else:
    print(0)