import tkinter as tk

MENUCOLOR = "#ff0000" # todo : remove or change to match windows calc? used so i can tell the difference in area atm
DISPLAYCOLOR = "#00fff0" # todo : remove or change to match windows calc? used so i can tell the difference in area atm

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.minsize(width=320, height=470)
        self.window.title("Calculator")

        self.menu_frame = create_menu_frame(self)

        self.current_display = "0: testing Current"
        self.history_display = "testing history"
        self.display_frame = create_display_frame(self)
        create_labels(self)

        self.button_frame = create_button_frame(self)
        create_buttons(self)

        configure_grids(self)

        self.window.mainloop()



def configure_grids(self):
    self.window.rowconfigure(1, weight=0)
    self.window.rowconfigure(2, weight=5)
    self.window.rowconfigure(3, weight=10)
    self.window.columnconfigure(0, weight=1)

    for x in range (6):
        self.button_frame.rowconfigure(x, weight=1)

    for x in range (4):
        self.button_frame.columnconfigure(x, weight=1)


def create_menu_frame(self):
    frame = tk.Frame(self.window, background=MENUCOLOR)
    menu = tk.Button(frame, height="2", width="5", text="Menu", background=MENUCOLOR)
    menu.grid(row=0, column=0, sticky="nsew")
    standard_label = tk.Label(frame, height="2", width="13", text="Standard", background=MENUCOLOR)
    standard_label.grid(row=0, column=1, sticky="nsew")
    on_top = tk.Button(frame, height="2", width="5", text="TOP", background=MENUCOLOR)
    on_top.grid(row=0, column=2, sticky="nsew")
    blank_label = tk.Label(frame, height="2", width="5", background=MENUCOLOR)
    blank_label.grid(row=0, column=3, sticky="nsew")
    history = tk.Button(frame, height="2", width="5", text="HIST", background=MENUCOLOR)
    history.grid(row=0, column=4, sticky="nsew")

    frame.columnconfigure(3, weight=1)

    frame.grid(row=0, sticky="nsew")
    return frame


def create_display_frame(self):
    frame = tk.Frame(self.window, background=DISPLAYCOLOR)
    frame.grid(row=2, column="0", sticky="nsew")
    return frame


def create_labels(self):
    label = tk.Label(self.display_frame, text=self.history_display, anchor="e", background=DISPLAYCOLOR, padx=5, font=("Calibri", 14))
    label.pack(expand="true", fill="both", side="top")
    label = tk.Label(self.display_frame, text=self.current_display, anchor="e", background=DISPLAYCOLOR, padx=20, font=("Calibir", 22))
    label.pack(expand="true", fill="both", side="bottom")


def create_button_frame(self):
    frame = tk.Frame(self.window)
    frame.grid(row=3, column="0", sticky="nsew")
    return frame

def create_buttons(self):
    # row 1
    modulo =        tk.Button(self.button_frame, text="%")#   ,  command=lambda:button_press("%"))
    clear_entry =   tk.Button(self.button_frame, text="CE")#  , command=button_clear)
    clear =         tk.Button(self.button_frame, text="C")#   ,  command=button_clear) # todo, update this to clear history row
    back =          tk.Button(self.button_frame, text="<-")
    modulo.grid(        row=0, column=0, sticky="NSEW", padx=1, pady=1)
    clear_entry.grid(   row=0, column=1, sticky="NSEW", padx=1, pady=1)
    clear.grid(         row=0, column=2, sticky="NSEW", padx=1, pady=1)
    back.grid(          row=0, column=3, sticky="NSEW", padx=1, pady=1)

    # row 2
    inverse =       tk.Button(self.button_frame, text="1/x")
    exponential =   tk.Button(self.button_frame, text="x^2")
    square_root =   tk.Button(self.button_frame, text="2√x")
    divide =        tk.Button(self.button_frame, text="÷")# , command=lambda:button_press("÷"))
    inverse.grid(       row=1, column=0, sticky="NSEW", padx=1, pady=1)
    exponential.grid(   row=1, column=1, sticky="NSEW", padx=1, pady=1)
    square_root.grid(   row=1, column=2, sticky="NSEW", padx=1, pady=1)
    divide.grid(        row=1, column=3, sticky="NSEW", padx=1, pady=1)

    # row 3
    seven =     tk.Button(self.button_frame, text="7")#, command=lambda:button_press(7))
    eight =     tk.Button(self.button_frame, text="8")#, command=lambda:button_press(8))
    nine =      tk.Button(self.button_frame, text="9")#, command=lambda:button_press(9))
    multiply =  tk.Button(self.button_frame, text="x")#, command=lambda:button_press("x"))
    seven.grid(     row=2, column=0, sticky="NSEW", padx=1, pady=1)
    eight.grid(     row=2, column=1, sticky="NSEW", padx=1, pady=1)
    nine.grid(      row=2, column=2, sticky="NSEW", padx=1, pady=1)
    multiply.grid(  row=2, column=3, sticky="NSEW", padx=1, pady=1)

    # row 4
    four =      tk.Button(self.button_frame, text="4")#, command=lambda:button_press(4))
    five =      tk.Button(self.button_frame, text="5")#, command=lambda:button_press(5))
    six =       tk.Button(self.button_frame, text="6")#, command=lambda:button_press(6))
    subtract =  tk.Button(self.button_frame, text="-")#, command=lambda:button_press("-"))
    four.grid(      row=3, column=0, sticky="NSEW", padx=1, pady=1)
    five.grid(      row=3, column=1, sticky="NSEW", padx=1, pady=1)
    six.grid(       row=3, column=2, sticky="NSEW", padx=1, pady=1)
    subtract.grid(  row=3, column=3, sticky="NSEW", padx=1, pady=1)

    # row 5
    one =   tk.Button(self.button_frame, text="1")#, command=lambda:button_press(1))
    two =   tk.Button(self.button_frame, text="2")#, command=lambda:button_press(2))
    three = tk.Button(self.button_frame, text="3")#, command=lambda:button_press(3))
    add =   tk.Button(self.button_frame, text="+")#, command=lambda:button_press('+'))
    one.grid(   row=4, column=0, sticky="NSEW", padx=1, pady=1)
    two.grid(   row=4, column=1, sticky="NSEW", padx=1, pady=1)
    three.grid( row=4, column=2, sticky="NSEW", padx=1, pady=1)
    add.grid(   row=4, column=3, sticky="NSEW", padx=1, pady=1)

    # row 6
    negative =  tk.Button(self.button_frame, text="+/-")
    zero =      tk.Button(self.button_frame, text="0")#, command=lambda:button_press(0))
    point =     tk.Button(self.button_frame, text=".")#, command=lambda:button_press("."))
    equals =    tk.Button(self.button_frame, text="=")
    negative.grid(  row=5, column=0, sticky="NSEW", padx=1, pady=1)
    zero.grid(      row=5, column=1, sticky="NSEW", padx=1, pady=1)
    point.grid(     row=5, column=2, sticky="NSEW", padx=1, pady=1)
    equals.grid(    row=5, column=3, sticky="NSEW", padx=1, pady=1)


def button_press_clear(self):
    pass

# def button_press(x):
#     """
#
#     :param x:
#     :return:
#     """
#     if current_input.cget('text') == "0":
#         if x == 0:
#             return
#         else:
#             current_input.config(text="")
#
#     if isinstance(x, int):
#         current_input.config(text=f"{current_input.cget('text')}{x}")
#     else:
#         current_history.config(text=f"{current_input.cget('text')} {x}")
#         current_input.config(text=f"need to update to show total") # todo update to show total but delete if a new int is typed
#
# def button_clear():
#     current_input.config(text="0")
#
#     def create_button(self):
#
#
#
# root = Tk()
# root.minsize(320,480)
# display = 0
#
# # Specify Grid
# Grid.rowconfigure(root, 0, minsize=15, weight=1)
# Grid.rowconfigure(root, 1, minsize=10, weight=1)
# Grid.rowconfigure(root, 2, minsize=40, weight=1)
# Grid.rowconfigure(root, 3, minsize=10, weight=1)
# Grid.rowconfigure(root, 4, minsize=20, weight=1)
# Grid.rowconfigure(root, 5, minsize=20, weight=1)
# Grid.rowconfigure(root, 6, minsize=20, weight=1)
# Grid.rowconfigure(root, 7, minsize=20, weight=1)
# Grid.rowconfigure(root, 8, minsize=20, weight=1)
# Grid.rowconfigure(root, 9, minsize=20, weight=1)
# Grid.columnconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 1, weight=1)
# Grid.columnconfigure(root, 2, weight=1)
# Grid.columnconfigure(root, 3, weight=1)
#
# # row 0
# menu = Button(root, text="Menu")
# calc_type = Label(root, text="Standard")
# on_top = Button(root, text="A_O_T")
# blank_space = Label(root, text="             ")
# show_history = Button(root, text="History")
# menu.grid(row=0, column=0, sticky="NSEW", padx=1, pady=1)
# calc_type.grid(row=0, column=1, sticky="NSEW", padx=1, pady=1)
# on_top.grid(row=0, column=2, sticky="NSEW", padx=1, pady=1)
# show_history.grid(row=0, column=3, sticky="NSEW", padx=1, pady=1)
#
# # row 1
# current_history = Label(root, anchor="e")
# current_history.grid(row=1, columnspan=4, sticky="NSEW")
#
# # row 2
# current_input = Label(root, text="0", anchor="e")
# current_input.grid(row=2, columnspan=4, sticky="NSEW")
#
# # row 3
# memory_clear = Button(root, state='disabled', text="MC")
# memory_recall = Button(root, state='disabled', text="MR")
# memory_add = Button(root, text="M+")
# memory_subtract = Button(root, text="M-")
# memory_store = Button(root, text="MS")
# show_memory = Button(root, state='disabled', text="M↓")
# memory_clear.grid(row=3, column=0, sticky="NSEW", padx=1, pady=1)
# memory_recall.grid(row=3, column=1, sticky="NSEW", padx=1, pady=1)
# memory_add.grid(row=3, column=2, sticky="NSEW", padx=1, pady=1)
# memory_subtract.grid(row=3, column=3, sticky="NSEW", padx=1, pady=1)
# memory_store.grid(row=3, column=4, sticky="NSEW", padx=1, pady=1)
# show_memory.grid(row=3, column=5, sticky="NSEW", padx=1, pady=1)
#
# # row 4
# modulo = Button(root, text="%", command=lambda:button_press("%"))
# clear_entry = Button(root, text="CE", command=button_clear)
# clear = Button(root, text="C", command=button_clear) # todo, update this to clear history row
# back = Button(root, text="<-")
# modulo.grid(row=4, column=0, sticky="NSEW", padx=1, pady=1)
# clear_entry.grid(row=4, column=1, sticky="NSEW", padx=1, pady=1)
# clear.grid(row=4, column=2, sticky="NSEW", padx=1, pady=1)
# back.grid(row=4, column=3, sticky="NSEW", padx=1, pady=1)
#
# # row 5
# inverse = Button(root, text="1/x")
# exponential = Button(root, text="x^2")
# square_root = Button(root, text="2√x")
# divide = Button(root, text="÷", command=lambda:button_press("÷"))
# inverse.grid(row=5, column=0, sticky="NSEW", padx=1, pady=1)
# exponential.grid(row=5, column=1, sticky="NSEW", padx=1, pady=1)
# square_root.grid(row=5, column=2, sticky="NSEW", padx=1, pady=1)
# divide.grid(row=5, column=3, sticky="NSEW", padx=1, pady=1)
#
# # row 6
# seven = Button(root, text="7", command=lambda:button_press(7))
# eight = Button(root, text="8", command=lambda:button_press(8))
# nine = Button(root, text="9", command=lambda:button_press(9))
# multiply = Button(root, text="x", command=lambda:button_press("x"))
# seven.grid(row=6, column=0, sticky="NSEW", padx=1, pady=1)
# eight.grid(row=6, column=1, sticky="NSEW", padx=1, pady=1)
# nine.grid(row=6, column=2, sticky="NSEW", padx=1, pady=1)
# multiply.grid(row=6, column=3, sticky="NSEW", padx=1, pady=1)
#
# # row 7
# four = Button(root, text="4", command=lambda:button_press(4))
# five = Button(root, text="5", command=lambda:button_press(5))
# six = Button(root, text="6", command=lambda:button_press(6))
# subtract = Button(root, text="-", command=lambda:button_press("-"))
# four.grid(row=7, column=0, sticky="NSEW", padx=1, pady=1)
# five.grid(row=7, column=1, sticky="NSEW", padx=1, pady=1)
# six.grid(row=7, column=2, sticky="NSEW", padx=1, pady=1)
# subtract.grid(row=7, column=3, sticky="NSEW", padx=1, pady=1)
#
# # row 8
# one = Button(root, text="1", command=lambda:button_press(1))
# two = Button(root, text="2", command=lambda:button_press(2))
# three = Button(root, text="3", command=lambda:button_press(3))
# add = Button(root, text="+", command=lambda:button_press('+'))
# one.grid(row=8, column=0, sticky="NSEW", padx=1, pady=1)
# two.grid(row=8, column=1, sticky="NSEW", padx=1, pady=1)
# three.grid(row=8, column=2, sticky="NSEW", padx=1, pady=1)
# add.grid(row=8, column=3, sticky="NSEW", padx=1, pady=1, )
#
# # row 9
# negative = Button(root, text="+/-")
# zero = Button(root, text="0", command=lambda:button_press(0))
# point = Button(root, text=".", command=lambda:button_press("."))
# equals = Button(root, text="=")
# negative.grid(row=9, column=0, sticky="NSEW", padx=1, pady=1)
# zero.grid(row=9, column=1, sticky="NSEW", padx=1, pady=1)
# point.grid(row=9, column=2, sticky="NSEW", padx=1, pady=1)
# equals.grid(row=9, column=3, sticky="NSEW", padx=1, pady=1)
#
# root.mainloop()
#
#
#
#
#

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
