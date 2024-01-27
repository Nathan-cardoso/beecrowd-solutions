#Resolução da questão 1042
#Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

n1, n2, n3 = map(int, input().split())

if (n1 < n2 and n1 < n3):
    if n2 < n3:
        print(n1)
        print(n2)
        print(n3)
    
    else:
        print(n1)
        print(n3)
        print(n2)

elif (n1 < n2 and n1 > n3):
        print(n3)
        print(n1)
        print(n2)
elif (n1 > n2 and n1 < n3):
        print(n2)
        print(n1)
        print(n3)
elif (n1 > n2 and n1 > n3):
    if n2 < n3:
        print(n2)
        print(n3)
        print(n1) 
    elif n3 < n2:
        print(n3)
        print(n2)
        print(n1)

print("")
print(n1)
print(n2)
print(n3)
