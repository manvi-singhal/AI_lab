# Minimax algorithm

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def get_winner(board):
    for player in ["X", "O"]:
        if check_winner(board, player):
            return player
    return None

def minimax(board, depth, is_maximizing):
    winner = get_winner(board)
    if winner:
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        else:
            return 0

    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def get_computer_move(board):
    best_score = float("-inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def main():
    board = [[" "]*3 for _ in range(3)]
    players = ["You", "Computer"]
    turn = 0
    
    print("Welcome to Tic Tac Toe!")
    print("Use positions 1-9 to place your move as follows:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\n\n")
    print_board(board)
    
    while True:
        player = players[turn % 2]
        
        if player == "You":
            while True:
                try:
                    position = int(input("Enter your move (1-9): "))
                    if 1 <= position <= 9:
                        row = (position - 1) // 3
                        col = (position - 1) % 3
                        if board[row][col] == " ":
                            break
                        else:
                            print("Position already taken. Please choose another position.")
                    else:
                        print("Position out of range. Please enter a number between 1 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            row, col = get_computer_move(board)
        
        if board[row][col] == " ":
            board[row][col] = "X" if player == "You" else "O"
            print_board(board)
            
            winner = get_winner(board)
            if winner:
                if winner == "X":
                    print("You win!")
                else:
                    print("Computer wins!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
            
            turn += 1
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()