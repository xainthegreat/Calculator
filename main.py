from tkinter import *

root = Tk()

root.minsize(319, 472)

# Specify Grid
Grid.rowconfigure(root, 0, minsize=15, weight=1)
Grid.rowconfigure(root, 1, minsize=10, weight=1)
Grid.rowconfigure(root, 2, minsize=40, weight=1)
Grid.rowconfigure(root, 3, minsize=10, weight=1)
Grid.rowconfigure(root, 4, minsize=20, weight=1)
Grid.rowconfigure(root, 5, minsize=20, weight=1)
Grid.rowconfigure(root, 6, minsize=20, weight=1)
Grid.rowconfigure(root, 7, minsize=20, weight=1)
Grid.rowconfigure(root, 8, minsize=20, weight=1)
Grid.rowconfigure(root, 9, minsize=20, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)

# row 0
menu = Button(root, text="Menu")
calc_type = Label(root, text="Standard")
on_top = Button(root, text="A_O_T")
blank_space = Label(root, text="             ")
show_history = Button(root, text="History")
menu.grid(row=0, column=0, sticky="NSEW", padx=1, pady=1)
calc_type.grid(row=0, column=1, sticky="NSEW", padx=1, pady=1)
on_top.grid(row=0, column=2, sticky="NSEW", padx=1, pady=1)
show_history.grid(row=0, column=3, sticky="NSEW", padx=1, pady=1)

# row 1
history = Label(root, text="history label temp string to show area", anchor="e")
history.grid(row=1, columnspan=4, sticky="NSEW")

# row 2
current = Label(root, text="0", anchor="e")
current.grid(row=2, columnspan=4, sticky="NSEW")

# row 3
memory_clear = Button(root, state='disabled', text="MC")
memory_recall = Button(root, state='disabled', text="MR")
memory_add = Button(root, text="M+")
memory_subtract = Button(root, text="M-")
memory_store = Button(root, text="MS")
show_memory = Button(root, state='disabled', text="M↓")
memory_clear.grid(row=3, column=0, sticky="NSEW", padx=1, pady=1)
memory_recall.grid(row=3, column=1, sticky="NSEW", padx=1, pady=1)
memory_add.grid(row=3, column=2, sticky="NSEW", padx=1, pady=1)
memory_subtract.grid(row=3, column=3, sticky="NSEW", padx=1, pady=1)
memory_store.grid(row=3, column=4, sticky="NSEW", padx=1, pady=1)
show_memory.grid(row=3, column=5, sticky="NSEW", padx=1, pady=1)

# row 4
modulo = Button(root, text="%")
clear_entry = Button(root, text="CE")
clear = Button(root, text="C")
back = Button(root, text="<-")
modulo.grid(row=4, column=0, sticky="NSEW", padx=1, pady=1)
clear_entry.grid(row=4, column=1, sticky="NSEW", padx=1, pady=1)
clear.grid(row=4, column=2, sticky="NSEW", padx=1, pady=1)
back.grid(row=4, column=3, sticky="NSEW", padx=1, pady=1)

# row 5
inverse = Button(root, text="1/x")
exponential = Button(root, text="x^2")
square_root = Button(root, text="2√x")
divide = Button(root, text="÷")
inverse.grid(row=5, column=0, sticky="NSEW", padx=1, pady=1)
exponential.grid(row=5, column=1, sticky="NSEW", padx=1, pady=1)
square_root.grid(row=5, column=2, sticky="NSEW", padx=1, pady=1)
divide.grid(row=5, column=3, sticky="NSEW", padx=1, pady=1)

# row 6
seven = Button(root, text="7")
eight = Button(root, text="8")
nine = Button(root, text="9")
multiply = Button(root, text="x")
seven.grid(row=6, column=0, sticky="NSEW", padx=1, pady=1)
eight.grid(row=6, column=1, sticky="NSEW", padx=1, pady=1)
nine.grid(row=6, column=2, sticky="NSEW", padx=1, pady=1)
multiply.grid(row=6, column=3, sticky="NSEW", padx=1, pady=1)

# row 7
four = Button(root, text="4")
five = Button(root, text="5")
six = Button(root, text="6")
subtract = Button(root, text="-")
four.grid(row=7, column=0, sticky="NSEW", padx=1, pady=1)
five.grid(row=7, column=1, sticky="NSEW", padx=1, pady=1)
six.grid(row=7, column=2, sticky="NSEW", padx=1, pady=1)
subtract.grid(row=7, column=3, sticky="NSEW", padx=1, pady=1)

# row 8
one = Button(root, text="1")
two = Button(root, text="2")
three = Button(root, text="3")
add = Button(root, text="+")
one.grid(row=8, column=0, sticky="NSEW", padx=1, pady=1)
two.grid(row=8, column=1, sticky="NSEW", padx=1, pady=1)
three.grid(row=8, column=2, sticky="NSEW", padx=1, pady=1)
add.grid(row=8, column=3, sticky="NSEW", padx=1, pady=1)

# row 9
negative = Button(root, text="+/-")
zero = Button(root, text="0")
point = Button(root, text=".")
equals = Button(root, text="=")
negative.grid(row=9, column=0, sticky="NSEW", padx=1, pady=1)
zero.grid(row=9, column=1, sticky="NSEW", padx=1, pady=1)
point.grid(row=9, column=2, sticky="NSEW", padx=1, pady=1)
equals.grid(row=9, column=3, sticky="NSEW", padx=1, pady=1)

root.mainloop()
