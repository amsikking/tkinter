import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_button()

    def init_button(self):
        self.button = tk.Button(self, text='print!', command=self.print)
        self.button.grid(row=0)

    def print(self):
        print('hello')

root = tk.Tk()
root.title('Button_GUI')

frame = TestFrame(root)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=1)

root.mainloop()
root.destroy()
