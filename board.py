def init_board():
    board = []

    for x in range(3):
        row = []
        for y in range(3):
            row.append(-1)

        board.append(row)

    return board


def check_win(board, player, x, y):
    row=col=diag=rdiag = 0
    for i in range(3):
        if board[x][i] == player:
            col += 1
        if board[i][y] == player:
            row += 1
        if board[i][i] == player:
            diag += 1
        if board[i][2 - i] == player:
            rdiag += 1

    if row == 3 or col == 3 or diag == 3 or rdiag == 3:
        return True
    else:
        return False


def make_move(board, player, x, y):
    if board[x][y] != -1:
        return False

    else:
        board[x][y] = player

        if check_win(board, player, x, y):
            print("Game over! Winner: " + str(player))
            exit(0)

        return True



def main():
    move_counter = 0
    board = init_board()

    while(True):
        player = move_counter % 2
        x = -1
        y = -1
        if player == 0:
            x = int(input("Player 0 please enter x coordinate"))
            y = int(input("Player 0 please enter y coordinate"))

        else:
            x = int(input("Player 1 please enter x coordinate"))
            y = int(input("Player 1 please enter y coordinate"))

        move_success = make_move(board, player, x, y)

        if move_success:
            move_counter += 1

        else:
            print("Invalid move, please try again.")

        print("\n")

        for row in board:
            print(row)

        print("\n")

main()