din = int(input())
pre = int(input())
des = int(input())


choco = din // pre

embalagem = choco
while embalagem >= des:
    embalagem -= des
    embalagem += 1
    choco += 1

print(choco)