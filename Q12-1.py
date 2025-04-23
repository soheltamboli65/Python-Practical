# Sohel Tamboli

import tkinter as tk

# Callback function to display "Hello, Button clicked!"
def on_hello_click():
    label.config(text="Hello, Button clicked!")

# Callback function to display "Good Bye!"
def on_goodbye_click():
    label.config(text="Good Bye!")

# Create the main window
window = tk.Tk()
window.title("Event Handling Example")

# Label to display messages
label = tk.Label(window, text="Press a button")
label.pack(pady=10)

# Button to trigger on_hello_click()
button_hello = tk.Button(window, text="Click Hello", command=on_hello_click)
button_hello.pack(pady=10)

# Button to trigger on_goodbye_click()
button_goodbye = tk.Button(window, text="Click Goodbye", command=on_goodbye_click)
button_goodbye.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
