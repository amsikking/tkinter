import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master, row):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(row=row, padx=20, pady=20)
        self.init_spinbox()

    def init_spinbox(self):
        self.spinbox_value = tk.StringVar()
        self.spinbox = tk.Spinbox(self,
                                  textvariable=self.spinbox_value,
                                  command=self.print,
                                  # or a tuple like values=('red', 'blu', 'grn')
                                  from_=0,
                                  to=10,
                                  increment=2)
        self.spinbox.bind("<Return>", self.entry_event)
        self.spinbox.bind("<FocusOut>", self.entry_event)
        self.spinbox.grid()

    def entry_event(self, event):
        self.print()

    def print(self):
        print(self.spinbox_value.get())

root = tk.Tk()
root.title('Spinbox_GUI')

frame1 = TestFrame(root, row=1)
frame2 = TestFrame(root, row=2)

# add close function + any commands for when the user hits the 'X'
def close():
    print('Closing')
    # close root window:
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
