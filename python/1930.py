# Problema 1930 - Tomadas

t1, t2, t3, t4 = map(int, input().split())

array_simple = [t1, t2, t3, t4]

sum = 0

for elemet in range(0,len(array_simple)):
    if elemet == len(array_simple) - 1:
        sum += array_simple[elemet]
    else:
        sum += array_simple[elemet] - 1

print(sum)

