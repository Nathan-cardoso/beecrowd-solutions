#Resolução d problema 1044
#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

n1, n2 = map(int,input().split())

if n1 >= n2:
    if n1 % n2 == 0.0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

else:
    if n2 % n1 == 0.0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')