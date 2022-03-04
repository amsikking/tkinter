import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_checkbutton()
        self.print()

    def init_checkbutton(self):
        self.checkbutton_value = tk.BooleanVar()
        self.checkbutton_value.set('True')
        self.checkbutton = tk.Checkbutton(
            self,
            text='print value',
            variable=self.checkbutton_value,
            command=self.print)
        self.checkbutton.grid(row=0)

    def print(self):
        print(self.checkbutton_value.get())

root = tk.Tk()
root.title('Button_GUI')

frame = TestFrame(root)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=1)

root.mainloop()
root.destroy()
