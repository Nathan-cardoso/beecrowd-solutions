tea = int(input())

value = input()

competitors = []

for i in value.split():
    competitors.append(int(i))

cont = 0

for j in competitors:
    if j == tea:
        cont += 1

print(cont)