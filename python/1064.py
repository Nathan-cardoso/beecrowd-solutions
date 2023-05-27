#Positivos e Média
valores = []

soma = positivos = 0
for i in range(6):
    valor = float(input())
    valores.append(valor)

for i in valores:
    if i > 0:
        positivos += 1
        soma += i

print(f'{positivos} valores positivos')
print('{:.1f}'.format(soma/positivos))
