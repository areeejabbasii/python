import tkinter as tk
import random
import time

def move_button():
    global start_time
    x = random.randint(50, 400)
    y = random.randint(50, 300)
    button.place(x=x, y=y)
    start_time = time.time()

def button_click():
    reaction_time = time.time() - start_time
    label.config(text=f"Reaction Time: {reaction_time:.3f} seconds")
    move_button()

root = tk.Tk()
root.title("Pop-up Reaction Game")
root.geometry("500x400")

label = tk.Label(root, text="Click the button as fast as you can!", font=("Arial", 14))
label.pack()

button = tk.Button(root, text="Click Me!", font=("Arial", 12), command=button_click)
button.place(x=200, y=150)

start_time = time.time()
move_button()

root.mainloop()
