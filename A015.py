eleitores = int(input())
brancos = int(input())
nulos = int(input())
validos = int(input())

porbranco = (brancos / eleitores) * 100
pornulo =  (nulos / eleitores) * 100
porvalidos = (validos / eleitores) * 100
ausentes = eleitores - brancos - nulos - validos
porausentes = (ausentes / eleitores) * 100

print(f'Nulos: {pornulo:.2f}%')
print(f'Brancos: {porbranco:.2f}%')
print(f'Validos: {porvalidos:.2f}%')
print(f'Ausentes: {porausentes:.2f}%')