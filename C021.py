numero1 = int(input())
soma = 0
unidades = 1
resto = 0
resto2 = 0
while unidades <= numero1*10:
    resto = numero1 % unidades
    soma = int(soma + (resto - resto2)//(unidades*0.1))
    resto2 = resto
    unidades = unidades * 10
print(f"{soma}")