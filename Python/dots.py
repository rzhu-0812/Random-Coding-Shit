from PIL import Image, ImageTk
import random
import tkinter as tk

window = tk.Tk()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
secret_code = [random.choice(colors) for _ in range(4)]
buttons = []
user_guess = []
row_index = 1

b_paths = [f"buttons/{color}_button.png" for color in colors]
d_paths = [f"dots/{color}_dot.png" for color in colors]
buttons = [ImageTk.PhotoImage(Image.open(path).resize((45, 30))) for path in b_paths]
dots = [ImageTk.PhotoImage(Image.open(path).resize((25, 25))) for path in d_paths]

def button_click(color):
  global row_index
  
  user_guess.append(color)
  show_dots()
  if len(user_guess) == 4:
    check_guess()
    row_index += 1
    user_guess.clear()

def show_dots():
  for i, color in enumerate(user_guess):
    dot_image = dots[colors.index(color)]
    dot = tk.Label(window, image=dot_image)
    dot.grid(row=row_index, column=i, padx=2)

def check_guess():
  for i, color in enumerate(user_guess):
    feedback_color = ("gray1" if color == secret_code[i] else
                      "gray99" if color in secret_code else
                      "gray50")

    label = tk.Label(window, text="●", fg=feedback_color, font=("Arial", 10))
    label.grid(row=row_index, column=i+4, padx=5)

for i, button in enumerate(buttons):
  button = tk.Button(window, image=button, relief=tk.FLAT, bd=0, command=lambda c=colors[i]: button_click(c))
  button.grid(row=0, column=i, padx=5)

print(secret_code)

window.mainloop()