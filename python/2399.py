inp  = int(input())
game = []

for i in range(0, inp):
    game.append(int(input()))

if len(game) == 1:
    print(game[0])

elif len(game) == 2:
    print(game[0] + game[1])

elif len(game) >= 3:
    result_game = []

    for j in range(0, inp):
        if j == 0:
            result_game.append(game[0] + game[1])
        elif j == inp-1:
            result_game.append(game[-2] + game[-1])
        else:
            result_game.append(game[j] + game[j - 1] + game[j + 1])

    for pr in result_game:
        print(pr)



            




