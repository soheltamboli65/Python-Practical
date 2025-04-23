# Sohel Tamboli

import tkinter as tk
from tkinter import ttk

def show():
    result.config(text=f"{combo.get()} | Likes: {'Yes' if var.get() else 'No'}")

root = tk.Tk()
combo = ttk.Combobox(root, values=["Apple", "Banana", "Cherry"])
combo.pack()

var = tk.BooleanVar()
tk.Checkbutton(root, text="I like it", variable=var).pack()

tk.Button(root, text="Click Me", command=show).pack()
result = tk.Label(root)
result.pack()

root.mainloop()
