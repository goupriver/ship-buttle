import random
import time

class Ship:
    def __init__(self, positions):
        self.positions = positions  # ?? массив [(x,y), (x,y)] - позиции точек корабля
        self.hits = []   # список - массив [(x, y), (x, y)] - список выстрелов по кораблю

    def is_sunk(self):
        return len(self.hits) == len(self.positions)

class Board:
    def __init__(self):
        self.board = [['O' for _ in range(6)] for _ in range(6)] # [[0,0,T,0,X],[],[]]   # доска
        self.ships = []      # Ship (ship.hits, ship.position)                           # корабли
        self.hits = set()    # множество {(x,y), (x,y)}                                  # удар

    def print_board(self):
        print('  | 1 | 2 | 3 | 4 | 5 | 6 |')
        for i, row in enumerate(self.board):
            print(f'{i+1} | {" | ".join(row)} |')

    def is_valid_position(self, x, y):
        if not (0 <= x < 6 and 0 <= y < 6):
            return False

        # for hit in self.hits:
        #     if abs(x - hit[0]) <= 1 and abs(y - hit[1]) <= 1:
        #         return False
        for hit in self.hits:
            if x == hit[0] and y == hit[1]:
                return False

        return True

    def is_hit(self, x, y):
        self.hits.add((x, y))  # добавить выстрел в Board.hits (x,y)
        for ship in self.ships:
            # если x,y в корабль.позиция есть
            if (x, y) in ship.positions:   # если в ships.ship.positon массиве есть (x,y) - координаты
                                           # positions может иметь вид {(2, 2), (2,3)} или [(2, 2), (2,3)] !
                ship.hits.append((x, y))     # добавить выстрел (x,y) в ship.hits
                # self.hits.add((x, y))        # добавить выстрел в Board.hits (x,y)
                self.board[y][x] = 'X'       # нарисовать 'X' на координате Board.board [y][x]
                return True                  # вернуть тру
        # нарисовать на доске 'T'
        self.board[y][x] = 'T'           # Board.board [y][x] = 'T'
        return False                     # вернуть фолс

# ПРОВЕРЕНО
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

def get_computer_move(board):
    while True:
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        if (x, y) not in board.hits:
            return x, y

def create_random_ships():
    ship_lengths = [3, 2, 2, 1, 1, 1, 1]
    ships = []
    for length in ship_lengths:
        positions = []
        while len(positions) < length:
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

def play_game():
    player_board = Board()
    computer_board = Board()

    player_board.ships = create_random_ships()
    computer_board.ships = create_random_ships()

    while True:
        print("Ваша доска:")
        player_board.print_board()
        print()
        print("Доска компьютера:")
        computer_board.print_board()
        print()

        player_x, player_y = get_player_move(computer_board)

        if computer_board.is_hit(player_x, player_y):
            print("Вы попали по кораблю противника!")
            if all(ship.is_sunk() for ship in computer_board.ships):
                print("Вы выиграли!")
                break
        else:
            print("Вы промахнулись!")


        computer_x, computer_y = get_computer_move(player_board)

        time.sleep(1)

        if player_board.is_hit(computer_x, computer_y):
            print("Компьютер попал по вашему кораблю!")
            if all(ship.is_sunk() for ship in player_board.ships):
                print("Компьютер выиграл!")
                break
        else:
            print("Компьютер промахнулся!")

        time.sleep(2)


play_game()