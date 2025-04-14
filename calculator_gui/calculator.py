from tkinter import *

root = Tk()
root.title('Calculator V1.0')

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Create functions for the buttns

def button_number(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_num = entry.get()
    global f_digg
    f_digg = int(first_num)
    entry.delete(0, END)


def button_equal():
    second_num = entry.get()
    entry.delete(0, END)
    entry.insert(0, f_digg + int(second_num))


# Creating button widgets and designing them

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_number(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_number(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_number(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_number(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_number(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_number(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_number(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_number(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_number(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_number(0))
add_button = Button(root, text='+', padx=40, pady=20, command= button_add)
equal_button = Button(root, text='=', padx=140, pady=20, command= button_equal)
clear_button = Button(root, text="C", padx=40, pady=20, command= button_clear)


# Aligning the buttons in order

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
clear_button.grid(row=4, column=1)
add_button.grid(row=4, column=2)
equal_button.grid(row=5, column=0, columnspan=3)

root.mainloop()