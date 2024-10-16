import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(padx=20, pady=20)
        self.init_entry()

    def init_entry(self):
        self.entry_value = tk.StringVar()
        register_entry = (self.register(self.validate), "%P")
        self.entrybox = tk.Entry(self,
                                 textvariable=self.entry_value,
                                 validate="all",
                                 validatecommand=register_entry)
        self.entrybox.grid(row=1)

    def validate(self, value):
        if (value.isdigit() and
            0 <= int(value) <= 100 and
            len(value) <= 3 or
            value == ''):
            valid = True
            print('Valid, value =', value)
        else:
            valid = False
            print('Error, value =', value,
                  'please choose integer in range 0-100')
        return valid

root = tk.Tk()
root.title('Entry_and_validation_GUI')

frame = TestFrame(root)

# add close function + any commands for when the user hits the 'X'
def close():
    print('Closing')
    # close root window:
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
