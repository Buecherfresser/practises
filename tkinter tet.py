import tkinter as tk


root = tk.Tk()
label = tk.Label(root, text="Hello World!") # Create a text label
label.pack(padx=20, pady=20) # Pack it into the window
T = tk.Text(root, height = 5, width = 52)
root.mainloop()

a