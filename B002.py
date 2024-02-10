limite = int(input())
multa = float(input())
adicional = float(input())
velocidade = int(input())

velo = velocidade - limite
adi = velo * adicional
if velocidade > limite:
    print(f'{multa + adi:.2f}')
else:
    print(f'{0:.2f}')
