cod,  qtd = map(int,input().split())

if cod == 1:
    preco = 4.0
    precoTotal = (float (preco * qtd)) 
elif cod == 2:
    preco = 4.50
    precoTotal = (float (preco * qtd)) 
elif cod == 3:
    preco = 5.0
    precoTotal = (float (preco * qtd)) 
elif cod == 4:
    preco = 2.0
    precoTotal = (float (preco * qtd)) 
elif cod == 5:
    preco = 1.50
    precoTotal = (float (preco * qtd)) 

print('Total: R$ {:.2f}'.format(precoTotal))



