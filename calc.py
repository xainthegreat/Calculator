import tkinter as tk

MENUCOLOR = "#ff0000" # todo : remove or change to match windows calc? used so i can tell the difference in area atm
DISPLAYCOLOR = "#00ff00" # todo : remove or change to match windows calc? used so i can tell the difference in area atm
MEMORYCOLOR = "#0000ff" # todo : remove or change to match windows calc? used so i can tell the difference in area atm

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.minsize(width=320, height=470)
        self.window.title("Calculator")

        self.menu_frame = create_menu_frame(self)

        self.current_display = "0"
        self.history_display = ""
        self.to_clear = False

        self.display_frame = create_display_frame(self)
        self.memory_frame = create_memory_frame(self)
        self.button_frame = create_button_frame(self)

        self.history_label, self.current_label = create_labels(self)
        create_buttons(self)

        configure_grids(self)

        self.window.mainloop()



def configure_grids(self):
    self.window.rowconfigure(0, weight=0)
    self.window.rowconfigure(1, weight=5)
    self.window.rowconfigure(2, weight=1)
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
    frame.grid(row=1, sticky="nsew")
    return frame


def create_labels(self):
    h_label = tk.Label(self.display_frame, text=self.history_display, anchor="e", background=DISPLAYCOLOR, padx=5, font=("Calibri", 14))
    h_label.pack(expand="true", fill="both", side="top")
    c_label = tk.Label(self.display_frame, text=self.current_display, anchor="e", background=DISPLAYCOLOR, padx=20, font=("Calibir", 22))
    c_label.pack(expand="true", fill="both", side="bottom")
    return h_label, c_label


def create_memory_frame(self):
    frame = tk.Frame(self.window, background=MEMORYCOLOR)

    memory_clear = tk.Button(frame, text="MC", background=MEMORYCOLOR)
    memory_clear.grid(row=0, column=0, sticky="nsew")
    memory_recall = tk.Button(frame, text="MR", background=MEMORYCOLOR)
    memory_recall.grid(row=0, column=1, sticky="nsew")
    memory_add = tk.Button(frame, text="M+", background=MEMORYCOLOR)
    memory_add.grid(row=0, column=2, sticky="nsew")
    memory_remove = tk.Button(frame, text="M-", background=MEMORYCOLOR)
    memory_remove.grid(row=0, column=3, sticky="nsew")
    memory_store = tk.Button(frame, text="MS", background=MEMORYCOLOR)
    memory_store.grid(row=0, column=4, sticky="nsew")
    memory_list = tk.Button(frame, text="M", background=MEMORYCOLOR)
    memory_list.grid(row=0, column=5, sticky="nsew")

    frame.rowconfigure(0, weight=1)
    for x in range(6):
        frame.columnconfigure(x, weight=1)

    frame.grid(row=2, sticky="nsew")

    return frame

def create_button_frame(self):
    frame = tk.Frame(self.window)
    frame.grid(row=3, sticky="nsew")
    return frame

def create_buttons(self):
    # row 1
    modulo =        tk.Button(self.button_frame, text="%")#,  command=lambda: button_press(self, "%"))
    clear_entry =   tk.Button(self.button_frame, text="CE", command=lambda: button_press_clear(self))
    clear =         tk.Button(self.button_frame, text="C",  command=lambda: button_press_clear(self)) # todo, update this to clear history row
    back =          tk.Button(self.button_frame, text="<-",  command=lambda: button_press_backspace(self))
    modulo.grid(        row=0, column=0, sticky="NSEW", padx=1, pady=1)
    clear_entry.grid(   row=0, column=1, sticky="NSEW", padx=1, pady=1)
    clear.grid(         row=0, column=2, sticky="NSEW", padx=1, pady=1)
    back.grid(          row=0, column=3, sticky="NSEW", padx=1, pady=1)

    # row 2
    inverse =       tk.Button(self.button_frame, text="1/x")
    exponential =   tk.Button(self.button_frame, text="x^2")
    square_root =   tk.Button(self.button_frame, text="2√x")
    divide =        tk.Button(self.button_frame, text="÷", command=lambda: button_press_symbol(self, "÷"))
    inverse.grid(       row=1, column=0, sticky="NSEW", padx=1, pady=1)
    exponential.grid(   row=1, column=1, sticky="NSEW", padx=1, pady=1)
    square_root.grid(   row=1, column=2, sticky="NSEW", padx=1, pady=1)
    divide.grid(        row=1, column=3, sticky="NSEW", padx=1, pady=1)

    # row 3
    seven =     tk.Button(self.button_frame, text="7", command=lambda: button_press_digit(self, 7))
    eight =     tk.Button(self.button_frame, text="8", command=lambda: button_press_digit(self, 8))
    nine =      tk.Button(self.button_frame, text="9", command=lambda: button_press_digit(self, 9))
    multiply =  tk.Button(self.button_frame, text="x", command=lambda: button_press_symbol(self, "x"))
    seven.grid(     row=2, column=0, sticky="NSEW", padx=1, pady=1)
    eight.grid(     row=2, column=1, sticky="NSEW", padx=1, pady=1)
    nine.grid(      row=2, column=2, sticky="NSEW", padx=1, pady=1)
    multiply.grid(  row=2, column=3, sticky="NSEW", padx=1, pady=1)

    # row 4
    four =      tk.Button(self.button_frame, text="4", command=lambda: button_press_digit(self, 4))
    five =      tk.Button(self.button_frame, text="5", command=lambda: button_press_digit(self, 5))
    six =       tk.Button(self.button_frame, text="6", command=lambda: button_press_digit(self, 6))
    subtract =  tk.Button(self.button_frame, text="-", command=lambda: button_press_symbol(self, "-"))
    four.grid(      row=3, column=0, sticky="NSEW", padx=1, pady=1)
    five.grid(      row=3, column=1, sticky="NSEW", padx=1, pady=1)
    six.grid(       row=3, column=2, sticky="NSEW", padx=1, pady=1)
    subtract.grid(  row=3, column=3, sticky="NSEW", padx=1, pady=1)

    # row 5
    one =   tk.Button(self.button_frame, text="1", command=lambda: button_press_digit(self, 1))
    two =   tk.Button(self.button_frame, text="2", command=lambda: button_press_digit(self, 2))
    three = tk.Button(self.button_frame, text="3", command=lambda: button_press_digit(self, 3))
    add =   tk.Button(self.button_frame, text="+", command=lambda: button_press_symbol(self, "+"))
    one.grid(   row=4, column=0, sticky="NSEW", padx=1, pady=1)
    two.grid(   row=4, column=1, sticky="NSEW", padx=1, pady=1)
    three.grid( row=4, column=2, sticky="NSEW", padx=1, pady=1)
    add.grid(   row=4, column=3, sticky="NSEW", padx=1, pady=1)

    # row 6
    negative =  tk.Button(self.button_frame, text="+/-", command=lambda: button_press_negative(self))
    zero =      tk.Button(self.button_frame, text="0", command=lambda: button_press_digit(self, 0))
    point =     tk.Button(self.button_frame, text=".", command=lambda: button_press_decimal(self))
    equals =    tk.Button(self.button_frame, text="=", command=lambda: button_press_equals(self))
    negative.grid(  row=5, column=0, sticky="NSEW", padx=1, pady=1)
    zero.grid(      row=5, column=1, sticky="NSEW", padx=1, pady=1)
    point.grid(     row=5, column=2, sticky="NSEW", padx=1, pady=1)
    equals.grid(    row=5, column=3, sticky="NSEW", padx=1, pady=1)


def button_press_digit(self, value):
    try:
        if self.history_display[-1] == "=":
            self.history_display = ""
            self.history_label.config(text=self.history_display)
    except:
        pass #todo do soemthing?

    if self.to_clear:
        self.current_display = ""
        self.to_clear = False

    if self.current_display == "0":
        if value == 0:
            return
        else:
            self.current_display = ""

    self.current_display += str(value)
    self.current_label.config(text=self.current_display)


def button_press_symbol(self, value):
    # todo update this to pull from history differently, equals button is going to screw this up
    if len(self.history_display) == 0:
        self.history_display = self.current_display + " " + str(value)
    else:
        temp_num = int(self.history_display[:-2])
        temp_sym = str(self.history_display[-1])
        if temp_sym == "+":
            temp_num += int(self.current_display)
        if temp_sym == "-":
            temp_num -= int(self.current_display)
        if temp_sym == "÷": #todo if round number drop decimal
            temp_num /= int(self.current_display)
        if temp_sym == "x":
            temp_num *= int(self.current_display)
        self.current_display = str(temp_num)
        self.history_display = str(temp_num) + " " + str(value)

    self.history_label.config(text=self.history_display)
    self.current_label.config(text=self.current_display)
    self.to_clear = True


def button_press_equals(self):
    # try:
    temp_num = int(self.history_display[:-2])
    temp_sym = str(self.history_display[-1])
    if temp_sym == "+":
        temp_num += int(self.current_display)
    if temp_sym == "-":
        temp_num -= int(self.current_display)
    if temp_sym == "÷":  # todo if round number drop decimal
        temp_num /= int(self.current_display)
    if temp_sym == "x":
        temp_num *= int(self.current_display)

    self.history_display = f"{self.history_display} {self.current_display} ="
    self.current_display = str(temp_num)
    self.history_label.config(text=self.history_display)
    self.current_label.config(text=self.current_display)
    # except:
    #     print("Error in button_press_equals")


def button_press_negative(self):
    if self.current_display == "0" or self.current_display == "0.":
        return

    temp = ""
    if self.current_display[0] == "-":
        temp = self.current_display[1:]
    else:
        temp += "-"
        temp += self.current_display

    self.current_display = temp
    self.current_label.config(text=self.current_display)


def button_press_decimal(self):
    if "." in self.current_display:
        return
    else:
        self.current_display += "."
        self.current_label.config(text=self.current_display)


def button_press_clear(self):
    self.current_display = "0"
    self.current_label.config(text=self.current_display)
    self.history_display = ""
    self.history_label.config(text=self.history_display)


def button_press_backspace(self):
    if len(self.current_display) == 1:
        self.current_display = "0"
    else:
        temp = self.current_display[:-1]
        self.current_display = temp

    self.current_label.config(text=self.current_display)



if __name__ == "__main__":
    calc = Calculator()
    calc.run()
