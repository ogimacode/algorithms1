num = int(input())

dias = num // 86400
restod = num % 86400
horas = restod // 3600
restoh = num % 3600
min = restoh // 60
seg = restoh % 60 

print(f'{dias} {horas} {min} {seg}')