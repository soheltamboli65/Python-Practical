# Sohel Tamboli

import tkinter as tk

def calculate(op):
    a, b = 10, 5
    result = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "division": "Cannot divide by zero" if b == 0 else a / b
    }[op]
    label.config(text=f"Result: {result}")

window = tk.Tk()
window.title("Simple Calc")

for op in ["Add", "Subtract", "Multiply", "Division"]:
    tk.Button(window, text=op, command=lambda O=op.lower(): calculate(O)).pack()

label = tk.Label(window, text="Result:")
label.pack()

window.mainloop()
