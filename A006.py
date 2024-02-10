valor = float(input())
porcentagem = float(input())

desconto = valor * porcentagem/100
dif = valor - desconto

print(f'{dif:.2f}')