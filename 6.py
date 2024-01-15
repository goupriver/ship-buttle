class Ship:
    def __init__(self, positions):
        self.positions = positions  # ?? массив [(x,y), (x,y)] - в зависимости какой длины корабль
        self.hits = []   # список - массив [(x, y), (x, y)]


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

def play_game():
    player_board = Board()
    computer_board = Board()

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




play_game()