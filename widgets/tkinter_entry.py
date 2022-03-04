import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master, row):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(row=row, padx=20, pady=20)
        self.init_entry()

    def init_entry(self):
        self.entry_value = tk.StringVar()
        self.entrybox = tk.Entry(self, textvariable=self.entry_value)
        self.entrybox.bind("<Return>", self.entry_event)
        self.entrybox.bind("<FocusOut>", self.entry_event)
        self.entrybox.grid()

    def entry_event(self, event):
        self.print()

    def print(self):
        print(self.entry_value.get())

root = tk.Tk()
root.title('Entry_GUI')

frame1 = TestFrame(root, row=1)
frame2 = TestFrame(root, row=2)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=3)

root.mainloop()
root.destroy()
