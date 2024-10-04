import tkinter as tk
import customtkinter as ctk

def click(row, col):
    print(f"Clicked on ({row}, {col})")

def create_grid(rows, columns):
    for row in range(rows):
        for column in range(columns):
            button = ctk.CTkButton(grid_frame, text="", width=25, height=25, command=lambda r=row, c=column: click(r, c))
            button.grid(row=row, column=column, padx=1, pady=1)
            button.configure(fg_color="white", hover_color="white")

def grid_size(state):
    if state == "Beginner":
        return 9, 9
    elif state == "Intermediate":
        return 16, 16
    elif state == "Expert":       
        return 16, 30

root = tk.Tk()
root.title("Minesweeper")

top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0)

difficulty_var = tk.StringVar()
difficulty_dropdown = ctk.CTkComboBox(top_frame, values=["Beginner", "Intermediate", "Expert"])
difficulty_dropdown.grid(row=0, column=0, padx=5, pady=5)
difficulty_dropdown.set("Intermediate")

reset_button = ctk.CTkButton(top_frame, text="", width=70, height=30)
reset_button.grid(row=0, column=1, padx=5, pady=5)
reset_button.configure(fg_color="white", hover_color="#F7F7F7")

grid_frame = tk.Frame(root)
grid_frame.grid(row=1, column=0)

root.mainloop()
