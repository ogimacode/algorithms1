pinos = list(map(int,input().split()))

placar = []
frame = []
contagem_frames = 0
pontos = 0

i = 0  # indice está contando os pinos
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 bolas possiveis
# I J
while contagem_frames < 9:
    #strike
    if pinos[i] == 10 and len(frame) == 0:
        pontos += 10
        frame.append(10)
        placar.append(frame)
        frame = []
        contagem_frames += 1
    # spare e pontos padrões
    else:
        frame.append(pinos[i])
        pontos += pinos[i]
    # a rodada do frame por completo
    if len(frame) == 2:
        placar.append(frame)
        frame = []
        contagem_frames += 1
    i += 1

# Ultimo frame
if contagem_frames == 9:
    frame = []
    while i < len(pinos):
        frame.append(pinos[i])
        pontos += pinos[i]
        i += 1
    placar.append(frame)

## Contagem do bonus + transferindo os valores para os simbolos
bonus = 0
# conta cada bola jogada 
bolas = 0
# conta os frames dentro do placar
i = 0
while i < contagem_frames:
    if len(placar[i]) == 1:
        bonus += pinos[bolas + 1] + pinos[bolas + 2]
        placar[i] = "X _"
        bolas += 1
    elif placar[i][0] + placar[i][1] == 10:
        placar[i][1] = "/"
        bonus += pinos[bolas + 2]
        bolas += 2
    else:
        bolas += 2
    i += 1
pontos = pontos + bonus

# Mudança dos simbolos do ultimo frame
ultimo = len(placar) - 1
if len(placar[ultimo]) == 3:
    i = 0
    while i < 3:
        if placar[ultimo][i] == 10:
            placar[ultimo][i] = "X"
        elif i < 2 and placar[ultimo][1] != "/":    
            if placar[ultimo][i] + placar[ultimo][i + 1] == 10:
                    placar[ultimo][i + 1] = "/"
        i += 1

# Impremindo o placar
for i in range(len(placar)):
    for j in range(len(placar[i])):
        print(placar[i][j] , end=" ")
    print(end="| ")
print()
print(pontos)