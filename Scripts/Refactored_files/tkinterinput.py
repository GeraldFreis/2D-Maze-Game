import tkinter as tk


"""
Globals
"""


name = str()
level = int()


"""
Creating a tkinter input window
"""


class Window:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('350x200+600+400')
        # self.win.colormapwindows('Blue')
        self.win.config(bg='Light Blue')  # creating a colour to match that of the pygame gui

    def creating_label(self, name, level):
        tk.Label(self.win, text="Enter name: ").grid(row=1)
        tk.Label(self.win, text="Enter level to play: ").grid(row=5)
        e = tk.Entry(self.win)
        en = tk.Entry(self.win)
        e.grid(row=1, column=1)
        en.grid(row=5, column=1)
        # self.win.mainloop()

        def get_values():  # returning values to use within the main script
            name_ = e.get()
            level_ = en.get()
            global name, level
            level = int(level_)
            name = str(name_)
            return name, level, self.win.destroy()
        tk.Button(self.win, text='Return Values', command=get_values).grid(row=6, column=1)
        self.win.mainloop()
        return name, level


win = Window()
win.creating_label(name, level)
