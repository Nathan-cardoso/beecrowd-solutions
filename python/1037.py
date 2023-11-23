numb = float(input())

if numb >= 0.0  and numb <= 25.0:
    print('Intervalo [0,25]')
elif numb > 25.0 and numb <= 50.0:
    print('Intervalo (25,50]')
elif numb > 50.0  and numb <= 75.0:
    print('Intervalo [50,75]')
elif numb > 75.0  and numb <= 100.0:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')