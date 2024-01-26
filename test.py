import random

class Board:
    def __init__(self):
        self.board = [['O' for _ in range(6)] for _ in range(6)] # [[0,0,T,0,X],[],[]]   # доска
        self.ships = []      # Ship (ship.hits, ship.position)                           # корабли
        self.hits = set()    # множество {(x,y), (x,y)}

    def is_valid_position(self, x, y):
        if not (0 <= x < 6 and 0 <= y < 6):
            return False
        for ship in self.ships:
            for sx, sy in ship.positions:
                if abs(x - sx) <= 1 and abs(y - sy) <= 1:
                    return False
        return True

    def is_hit(self, x, y):
        for ship in self.ships:
            if (x, y) in ship.positions:   # если в ships.ship.positon массиве есть (x,y) - координаты
                ship.hits.append((x, y))     # добавить выстрел (x,y) в ship.hits
                self.hits.add((x, y))        # добавить выстрел в Board.hits (x,y)
                self.board[y][x] = 'X'       # нарисовать 'X' на координате Board.board [y][x]
                return True                  # вернуть тру
        self.board[y][x] = 'T'           # Board.board [y][x] = 'T'
        return False                     # вернуть фолс

def get_player_move(board):
    while True:
        try:
            x = int(input("Введите номер столбца (1-6): ")) - 1
            y = int(input("Введите номер строки (1-6): ")) - 1
            if (x, y) in board.hits:
                raise ValueError("Вы уже стреляли в эту клетку!")
            if not board.is_valid_position(x, y):
                raise ValueError("Неверный ход!")
            return x, y
        except ValueError as e:
            print(e)

# print(get_player_move(Board()))
class Ship:
    def __init__(self, positions):
        self.positions = positions
        self.hits = []


def create_random_ships():
    ship_lengths = [3, 2, 2, 1, 1, 1, 1]
    ships = []
    for length in ship_lengths:
        positions = []
        while len(positions) < length:   # 0 < 3
            valid_positions = []
            for x in range(6):
                for y in range(6):
                    if (x, y) not in positions and Board().is_valid_position(x, y):
                        valid_positions.append((x, y))

            if len(valid_positions) == 0:
                break

            x, y = random.choice(valid_positions)
            positions.append((x, y))
        ships.append(Ship(positions))

    return ships

positions = []
valid_positions = []
for x in range(6):
    for y in range(6):
        if (x, y) not in positions and Board().is_valid_position(x, y):
            valid_positions.append((x, y))

