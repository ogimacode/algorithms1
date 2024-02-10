def palavra_igual(palavra1, palavra2):
    for i in range(len(palavra1)):
        if palavra1[i] != palavra2[i]:
            return False
    return True

palavra1 = input()
palavra2 = input()

if palavra_igual(palavra1, palavra2):
    print('True')
else:
    print('False')