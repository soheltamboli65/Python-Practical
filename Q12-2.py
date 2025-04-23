#Sohel Tamboli


import tkinter as tk
from tkinter import ttk

# Corrected exchange rates dictionary (no colons in keys)
rates = {
    "USD": 1.0,
    "INR": 83.27,
    "EURO": 0.92
}

def convert():
    try:
        amt = float(entry.get())
        from_curr = from_combo.get()
        to_curr = to_combo.get()
        usd_amt = amt / rates[from_curr]
        result = usd_amt * rates[to_curr]
        label_result.config(text=f"{amt} {from_curr} = {result:.2f} {to_curr}")
    except:
        label_result.config(text="Invalid input.")

# GUI setup
window = tk.Tk()
window.title("Currency Converter")

tk.Label(window, text="Amount:").pack()
entry = tk.Entry(window)
entry.pack()

tk.Label(window, text="From Currency:").pack()
from_combo = ttk.Combobox(window, values=list(rates.keys()))
from_combo.pack()

tk.Label(window, text="To Currency:").pack()
to_combo = ttk.Combobox(window, values=list(rates.keys()))
to_combo.pack()

tk.Button(window, text="Convert", command=convert).pack(pady=10)

label_result = tk.Label(window, text="Result will appear here")
label_result.pack(pady=10)

window.mainloop()
