 #Maior e Posição     

value = []
for i in range(100):
    valor = int(input())
    value.append(valor)

bigger = value[0]
index = 0
for i in range(100):
    if value[i] > bigger:
        bigger = value[i]
        index = i+1

print(bigger)
print(index)
    