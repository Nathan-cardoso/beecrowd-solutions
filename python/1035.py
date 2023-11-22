a, b, c, d = map(int, input().split())

soma1 = c + d
soma2 = a + b

if (b > c) and (d > a) and (soma1 > soma2) and (c > 0 and d > 0) and (a % 2 == 0):
    print('Valores aceitos')
else:
    print("Valores nao aceitos")