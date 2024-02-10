salario = float(input())
vendas = float(input())

adicional = vendas * 0.18
total = salario + adicional

print(f'{total:.2f}')