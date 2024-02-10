n = int(input())

sequencia = 1
maior_sequencia = 1

if n > 0:

    num1 = int(input())

    i = 1
    while i < n:
        num2 = int(input())
        if num2 >= num1:
            sequencia += 1
        else:
            sequencia = 1
        if sequencia > maior_sequencia:
            maior_sequencia = sequencia
        num1 = num2            
        i += 1
    print(maior_sequencia)
    
else:
    print("Valor invalido.")