n = int(input())
x = int(input())

participantes = []
restantes = []
eliminado_x = 0
eliminados = 0
for i in range(1, n + 1):
    participantes.append(i)

i = 0
impostor = True
while len(participantes) != 1:
    j = 0
    while j < len(participantes):
        if impostor == True:
            restantes.append(participantes[j])
            impostor = False
        else:
            impostor = True
            eliminados += 1
            if eliminados == x:
                eliminado_x = participantes[j]
        j += 1
    participantes = restantes
    restantes = []
    i += 1

ganhas = participantes[0]
print(f'Eliminação {x}: {eliminado_x}')
print(f'Ganhadora: {ganhas}')