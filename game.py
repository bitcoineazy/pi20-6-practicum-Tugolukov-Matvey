#table = [['*'] * 5 for _ in range(4)]
players_char = ['1', '2', '3']


width = 5 # размерность массива (квадратная матрица)
height = 4
table = [['*'] * 5 for _ in range(4)]
def draw_board(a: list):
    print("-" * (len(table) * 5 + 1))
    for i in range(len(a)):
        print("|", end="")
        for j in range(len(a[0])):
            print(f" {a[i][j]} |", end="")
        # a[i][j] - это и есть обращение к элементу двумерного массива
        print("\n" + "-" * (len(table) * 5 + 1))





for i in range(20):
    player = i % 3
    x, y = map(int, input(f'Ход игрока {player + 1}: ').split())
    try:
        table[y - 1][x - 1] = players_char[player]
    except:
        print('Введите нормальные числа')
        continue
    draw_board(table)

dxy = [[-1, -1], [-1, 0], [-1, 1], \
       [0,  -1],          [0,  1], \
       [1,  -1], [1,  0], [1,  1]  ]
score = [0, 0, 0]
for y in range(4):
    for x in range(5):
        for i in range(len(dxy)):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < 5 and 0 <= ny < 4:
                if table[y][x] == table[ny][nx]:
                    score[int(table[y][x]) - 1] += 1
                    # Для иных символов игроков нужно составить словарь
                    # char_rev = {player_char[i]: i for i in range(len(player))}
                    # И использовать score[char_rev[table[y][x]]]

# Теперь в score удвоенное количество штрафных очков каждого игрока
# Так что их все нужно поделить на 2
score = [i // 2 for i in score]

for i in range(len(player)):
    print(f'Игрок {i + 1} получил {score[i]} штрафных очков')

# Тут далее необходимо расписать возможные случаи:
# 1) Победил один игрок - у него меньше очков, чем у двух других
# 2) Победили два игрока - у них одинаковое количество очков, меньшее, чем у третьего
# 3) Полная ничья - у всех игроков одинаковое количество очков
# После чего вывести соответствующее сообщение о победе
