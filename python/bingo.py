import tkinter as tk
import random

def generate_bingo_card():
    numbers = {col: random.sample(range(start, start + 15), 5) for col, start in zip(range(5), range(1, 76, 15))}
    numbers[2][2] = "FREE"  # Free space in the center
    return [[numbers[col][row] for col in range(5)] for row in range(5)]

def check_bingo():
    for row in range(5):
        if all(buttons[row][col]['bg'] == 'green' for col in range(5)):
            result_label.config(text=f"{current_player} wins!")
            return
    for col in range(5):
        if all(buttons[row][col]['bg'] == 'green' for row in range(5)):
            result_label.config(text=f"{current_player} wins!")
            return
    if all(buttons[i][i]['bg'] == 'green' for i in range(5)) or all(buttons[i][4-i]['bg'] == 'green' for i in range(5)):
        result_label.config(text=f"{current_player} wins!")
        return

def mark_number(row, col):
    global current_player
    if buttons[row][col]['bg'] != 'green':
        buttons[row][col].config(bg='green')
        check_bingo()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "Player 1" if current_player == "Player 2" else "Player 2"
    turn_label.config(text=f"{current_player}'s Turn")

root = tk.Tk()
root.title("Bingo Game - Two Players")
root.geometry("600x500")

frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT, padx=20, pady=20)

frame2 = tk.Frame(root)
frame2.pack(side=tk.RIGHT, padx=20, pady=20)

current_player = "Player 1"
board = generate_bingo_card()
buttons = [[None for _ in range(5)] for _ in range(5)]

for r in range(5):
    for c in range(5):
        btn = tk.Button(frame1, text=str(board[r][c]), font=("Arial", 16), width=5, height=2, command=lambda r=r, c=c: mark_number(r, c))
        btn.grid(row=r, column=c)
        buttons[r][c] = btn

turn_label = tk.Label(frame2, text=f"{current_player}'s Turn", font=("Arial", 16))
turn_label.pack(pady=10)

result_label = tk.Label(frame2, text="", font=("Arial", 16))
result_label.pack(pady=10)

root.mainloop()
