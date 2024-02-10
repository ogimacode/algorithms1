def palavra_diferente(palavra):
    i = 0
    while i < len(palavra):
        j = i + 1
        while j < len(palavra):
            if palavra[i] == palavra[j]:
                return False
            j += 1
        i += 1
    return True


palavra = input()

if palavra_diferente(palavra):
    print('Não repete')
else:
    print('Repete')