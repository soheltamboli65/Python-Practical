import tkinter as tk

root = tk.Tk()
root.title("Image Display")

# Load the .gif image (ensure it's a valid .gif file)
image = tk.PhotoImage(file="C:/Users/ijaj/Desktop/Sohel.png")

# Display the image in the Tkinter window
label = tk.Label(root, image=image)
label.pack()

# Run the Tkinter main loop
root.mainloop()
