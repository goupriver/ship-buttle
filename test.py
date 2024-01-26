board = [['O' for _ in range(6)] for _ in range(6)]
board2 = [['1' for _ in range(6)] for _ in range(6)]

print("       Доска противника                     Ваша Доска")
print("  | 1 | 2 | 3 | 4 | 5 | 6 |          | 1 | 2 | 3 | 4 | 5 | 6 |")
for i, row in enumerate(board):
    print(f'{i+1} | {" | ".join(board[i])} |        {i+1} | {" | ".join(board2[i])} |')

