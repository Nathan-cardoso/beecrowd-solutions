 #Maior e Posição     

valores = []
for i in range(100):
    valor = int(input())
    valores.append(valor)

maior = valores[0]
index = 0
for i in range(100):
    if valores[i] > maior:
        maior = valores[i]
        index = i+1

print(maior)
print(index)
    