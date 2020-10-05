players_char = ['1', '2', '3']
width = 5
height = 4
table = [['*'] * width for i in range(height)]

def draw_board(a):
    print("-" * (len(table) * 5 + 1))
    for i in range(len(a)):
        print("|", end="")
        for j in range(len(a[0])):
            print(f" {a[i][j]} |", end="")
        print("\n" + "-" * (len(table) * 5 + 1))

print('"Лоскутное одеяло" игра для 3-х игроков')
draw_board(table)
print('Введите координаты хода в через пробел формате: НОМЕР_В_СТРОКЕ НОМЕР_СТОЛБЦА \nШтрафные очки подсчитываются в конце игры')



current_move = 0
while current_move < 20:
        player = current_move % 3
        try:
            x, y = map(int, input(f'Ход игрока {player + 1}: ').split())
        except:
            print('Введите числа в формате: НОМЕР_В_СТРОКЕ НОМЕР_СТОЛБЦА')
            continue
        try:
            if table[y - 1][x - 1] == "*":
                table[y - 1][x - 1] = players_char[player]
            elif table[y - 1][x - 1] != "*":
                print('Поле уже занято')
                current_move -= 1
            elif 'end' in x or y:
                break
        except:
            print('Введите числа удовлетворяющие кол-ву строк(1-5) и кол-ву столбцов(1-4)')
            continue
        draw_board(table)
        current_move += 1

#это дельты соответственных координат по различным направлениям в одномерном массиве пар
#для каждого направления прописал, какие координаты у клетки-соседа в этом направлении относительно изначальной.
dxy = [[-1, -1], [-1, 0], [-1, 1],
       [0,  -1],          [0,  1],
       [1,  -1], [1,  0], [1,  1]  ]
score = [0, 0, 0]

for y in range(height):
    for x in range(width):
        for i in range(len(dxy)):
            nx, ny = x + dxy[i][0], y + dxy[i][1] #nx, ny - это координаты клетки-соседа в i-том направлении
            if 0 <= nx < 5 and 0 <= ny < 4:
                if table[y][x] == table[ny][nx]:
                    try:
                        score[int(table[y][x]) - 1] += 1
                    except ValueError:
                        print('Что-то определённо не так')
                        continue

#Теперь в score удвоенное количество штрафных очков каждого игрока
#Так что их все нужно поделить на 2
score = [i // 2 for i in score]
for i in range(len(players_char)):
    print(f'Игрок {i + 1} получил {score[i]} штрафных очков')

if score[0] < score[1] and score[0] < score[2]:
    print(f'Победил 1-ый игрок')
elif score[1] < score[0] and score[1] < score[2]:
    print(f'Победил 2-ой игрок')
elif score[2] < score[0] and score[2] < score[1]:
    print(f'Победил 3-ий игрок')
elif (score[0] == score[1]) and score[0] < score[2] and score[1] < score[2]:
    print(f'Победили два игрока 1 и 2')
elif (score[1] == score[2]) and score[1] < score[0] and score[2] < score[0]:
    print(f'Победили два игрока 2 и 3 ')
elif (score[0] == score[2]) and score[0] < score[1] and score[2] < score[1]:
    print(f'Победили два игрока 1 и 3')
elif score[0] == score[1] == score[2]:
    print(f'Полная ничья!')
