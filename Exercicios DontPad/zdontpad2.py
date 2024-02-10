def compara_string(s1, s2):
    igual = True
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            igual = False
            break
    return igual

s1 = input()
s2 = input()

if compara_string(s1, s2):
    print("True")
else:
    print("False")