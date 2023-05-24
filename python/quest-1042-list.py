#Resolução da questão 1042 utilizando listas
#Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

num1, num2, num3 = map(int, input().split())

list = [num1, num2, num3]
sortList = [int(i) for i in list]

sortList.sort()

print(*sortList, sep='\n')
print('')
print(*list, sep='\n')
