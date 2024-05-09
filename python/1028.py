def gcd(a, b):
  ''' GCD (greatest commom divisor) It's an algorithm for finding the greatest common divisor.
      This algorithm is known as Euclid's algorithm and to understand how it works and examples, search the link below.
      link: https://www.freecodecamp.org/portuguese/news/algoritmo-de-euclides-mdc-maximo-divisor-comum-explicado-com-exemplos-em-varias-linguagens/'''
  
  if b == 0:
    return a
  else:
    return gcd(b, (a % b))
  
#Solução da questão 1028 - Figurinhas.

numb_input = int(input())
result = []

for i in range(0, numb_input):
    input_figures = input()
    figure1, figure2 = (int(num) for num in input_figures.split(' ') )
    result.append(gcd(figure1, figure2))

for r in result:
   print(r)



