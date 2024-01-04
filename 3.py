import random

class Ship:
    def __init__(self, positions):
        self.positions = positions
        self.hits = []

    def is_sunk(self):
        return len(self.hits) == len(self.positions)

class Board:
    def __init__(self):
        self.board = [['O' for _ in range(6)] for _ in range(6)]
        self.ships = []
        self.hits = set()

    def place_ship(self, ship):
        for x, y in ship.positions:
            self.board[y][x] = '■'
        self.ships.append(ship)

    def print_board(self):
        print('   | 1 | 2 | 3 | 4 | 5 | 6|')
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
            if (x, y) in ship.positions:
                ship.hits.append((x, y))
                self.hits.add((x, y))
                self.board[y][x] = 'X'
                return True
        self.board[y][x] = 'T'
        return False

def create_random_ships():
    ship_lengths = [3, 2, 2, 1, 1, 1, 1]
    ships = []
    for length in ship_lengths:
        positions = []
        while len(positions) < length:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if (x, y) not in positions and board.is_valid_position(x, y):
                positions.append((x, y))
        ships.append(Ship(positions))
    return ships

def play_game():
    player_board = Board()
    computer_board = Board()

    player_ships = create_random_ships()
    computer_ships = create_random_ships()

    for ship in player_ships:
        player_board.place_ship(ship)
    for ship in computer_ships:
        computer_board.place_ship(ship)

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

        if player_board.is_hit(computer_x, computer_y):
            print("Компьютер попал по вашему кораблю!")
            if all(ship.is_sunk() for ship in player_board.ships):
                print("Компьютер выиграл!")
                break
        else:
            print("Компьютер промахнулся!")

play_game()