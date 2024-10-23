def print_board(board):
    for i in range(len(board)):
        print(" | ".join(board[i]))
        if i!=2:
            print("-"*9)
    #print(board)
    return True

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            try:
                row = int(input("Enter the row (1, 2, or 3): ")) - 1
                col = int(input("Enter the column (1, 2, or 3): ")) - 1
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already occupied! Choose another one.")
            except (IndexError, ValueError):
                print("Invalid input! Enter numbers between 1 and 3.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
