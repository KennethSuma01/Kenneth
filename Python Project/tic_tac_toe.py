import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True, row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True, board[0][2]

    return False, None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def on_button_click(row, col):
    global current_player, board_buttons

    if board[row][col] != ' ':
        return

    board_buttons[row][col].config(text=current_player, state=tk.DISABLED)
    board[row][col] = current_player

    # Check for a winner
    winner_found, winner = check_winner(board)
    if winner_found:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset_board()
        return

    # Check for a draw
    if is_board_full(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()
        return

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

def reset_board():
    global current_player, board_buttons, board
    current_player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            board_buttons[i][j].config(text=' ', state=tk.NORMAL)

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize game variables
current_player = 'X'
board = [[' ' for _ in range(3)] for _ in range(3)]

# Create board buttons
board_buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('Arial', 20), width=4, height=2,
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(button)
    board_buttons.append(row_buttons)

# Create reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_board)
reset_button.grid(row=3, columnspan=3, pady=10)

root.mainloop()
