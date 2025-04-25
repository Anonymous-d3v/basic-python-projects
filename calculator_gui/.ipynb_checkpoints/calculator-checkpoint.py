import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import datetime, timezone


root = tb.Window(themename="cyborg")
root.title('Calculator V1.0')

entry = tb.Entry(root, width=35)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#entry.config(state=DISABLED)

#Create functions for the buttons

def button_number(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_num = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    entry.delete(0, END)



def show_hist():
    child = tb.Toplevel(root)
    child.title("Calculator History")
    child.geometry("400x250")
    query_box = tb.Text(child, font=("Courier New", 11))
    query_box.pack(padx=10, pady=10)
    try:
        with open('calc_hist.txt', 'r') as hist_file:
            query_box.config(state=NORMAL)
            query_box.delete("1.0", END)
            query_box.insert(END, hist_file.read())
            query_box.config(state=DISABLED)
    except FileNotFoundError:
        query_box.insert(END, "No history found.")
        query_box.config(state=DISABLED)

    tb.Button(child, text="Close", command=child.destroy).pack()
    


def button_equal():
    second_num: str = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + int(second_num))
        with open('calc_hist.txt', 'a') as hf:
            hf.write(f'\n{f_num} + {int(second_num)} = {entry.get()} | Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            hf.close
    elif math == "subtraction":
        entry.insert(0, f_num - int(second_num))
        with open('calc_hist.txt', 'a') as hf:
            hf.write(f'\n{f_num} - {int(second_num)} = {entry.get()} | Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            hf.close
    elif math == "multiplication":
        entry.insert(0, f_num * int(second_num))
        with open('calc_hist.txt', 'a') as hf:
            hf.write(f'\n{f_num} * {int(second_num)} = {entry.get()} | Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            hf.close
    elif math == "division":
        entry.insert(0, f_num / int(second_num))
        with open('calc_hist.txt', 'a') as hf:
            hf.write(f'\n{f_num} / {int(second_num)} = {entry.get()} | Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            hf.close
    else:
        return


def button_sub():
    first_num = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    entry.delete(0, END)


def button_multi():
    first_num = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    entry.delete(0, END)


def button_divide():
    first_num = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    entry.delete(0, END)



# Creating button widgets and designing them

button_1 = tb.Button(root, text="1", command=lambda: button_number(1))
button_2 = tb.Button(root, text="2", command=lambda: button_number(2))
button_3 = tb.Button(root, text="3", command=lambda: button_number(3))
button_4 = tb.Button(root, text="4", command=lambda: button_number(4))
button_5 = tb.Button(root, text="5", command=lambda: button_number(5))
button_6 = tb.Button(root, text="6", command=lambda: button_number(6))
button_7 = tb.Button(root, text="7", command=lambda: button_number(7))
button_8 = tb.Button(root, text="8", command=lambda: button_number(8))
button_9 = tb.Button(root, text="9", command=lambda: button_number(9))
button_0 = tb.Button(root, text="0", command=lambda: button_number(0))

add_button = tb.Button(root, text='+', command=button_add)
equal_button = tb.Button(root, text='=', command=button_equal)
clear_button = tb.Button(root, text="C", command=button_clear)
subtract_button = tb.Button(root, text='-', command=button_sub)
multiply_button = tb.Button(root, text='*', command=button_multi)
divide_button = tb.Button(root, text='/', command=button_divide)
hist_button = tb.Button(root, text='Show History', command=show_hist)


# Aligning the buttons in order
button_1.grid(row=3, column=0, padx=5, pady=5)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)

button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0, padx=5, pady=5)
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9.grid(row=1, column=2, padx=5, pady=5)

button_0.grid(row=4, column=0, padx=5, pady=5)
clear_button.grid(row=4, column=1, padx=5, pady=5)
equal_button.grid(row=4, column=2, padx=5, pady=5)

add_button.grid(row=5, column=0, padx=5, pady=5)
subtract_button.grid(row=5, column=1, padx=5, pady=5)
multiply_button.grid(row=5, column=2, padx=5, pady=5)
divide_button.grid(row=6, column=0, padx=5, pady=5)

hist_button.grid(row=6, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

root.mainloop()