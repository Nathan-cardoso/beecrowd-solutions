def gcd(a, b):
  ''' GCD (greatest commom divisor) trata-se de um algoritmo para encontrar o máximo divisor comum.
      Esse algoritmo é conhecido como algoritmo de Euclides e para entender seu funcionamento e exemplos pesquise no link abaixo
      link: https://www.freecodecamp.org/portuguese/news/algoritmo-de-euclides-mdc-maximo-divisor-comum-explicado-com-exemplos-em-varias-linguagens/'''
  
  if b == 0:
    return a
  else:
    return gcd(b, (a % b))
  


numb_input = int(input())
result = []

for i in range(0, numb_input):
    input_figures = input()
    figure1, figure2 = (int(num) for num in input_figures.split(' ') )
    result.append(gcd(figure1, figure2))

for r in result:
   print(r)



