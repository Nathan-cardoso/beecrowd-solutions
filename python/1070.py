#Resolução do problema 1070
#Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

x = int(input())

if(x % 2 == 0):
    x += 1
    for i in range(6):
        print(x)
        x += 2
    
else:
    for i in range(6):
        print(x)
        x += 2


