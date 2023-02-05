board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = "X"


def print_board():
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print("---+---+---")
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print("---+---+---")
    print(f' {board[7]} | {board[8]} | {board[9]} ')


def check_win():
    if board[1] == board[2] == board[3] != ' ':
        return board[1]
    if board[4] == board[5] == board[6] != ' ':
        return board[4]
    if board[7] == board[8] == board[9] != ' ':
        return board[7]
    if board[1] == board[4] == board[7] != ' ':
        return board[1]
    if board[2] == board[5] == board[8] != ' ':
        return board[2]
    if board[3] == board[6] == board[9] != ' ':
        return board[3]
    if board[1] == board[5] == board[9] != ' ':
        return board[1]
    if board[3] == board[5] == board[7] != ' ':
        return board[3]
    if ' ' not in board:
        return "TIE"
    return None


while True:
    print_board()
    move = int(input(f'Player {player}, enter your move (1-9): '))
    if board[move] != ' ':
        print("Invalid move, try again")
        continue
    board[move] = player
    winner = check_win()
    if winner:
        print_board()
        print(f'Player {winner} wins!')
        break
    player = "O" if player == "X" else "X"
