semana = 7
list = []
i = 0
dias = 0
while i < semana:
    temp = float(input())
    list.append(temp)
    dias += temp
    i += 1
media = dias / semana

i = 0
temp_alta = 0
while i <= 6:
    if list[i] > media:
        temp_alta += 1
    i += 1
print(temp_alta)