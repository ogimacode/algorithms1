n = int(input())
soma = 0       
while n > 0:
    divisores = 1
    i = 1
    if (n !=  2 and n % 2 == 0):
        n += (-1)
    else:    
        while i <= (n/2) and n > 1:
            if n % i == 0:
                divisores += 1
            i += 1    
        if divisores == 2 and n != 1:
            soma += n
        if n <= 3:
            n += (-1)
        else:        
            n += (-2)
print(soma)