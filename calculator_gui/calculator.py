from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# You can add the rest of the calculator code later
root.mainloop()
