import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid(padx=20, pady=20)
        self.init_slider()

    def init_slider(self):
        default = 10
        self.slider_value = tk.IntVar()
        self.slider_value.set(default)
        self.slider = tk.Scale(self,
                               command=self.print,
                               from_=0,
                               to=100,
                               tickinterval=20,
                               orient='horizontal',
                               length=300,
                               variable=self.slider_value)
        self.slider.grid(row=1)

    def print(self, scale_value):       # scale_value variable is required
        print(self.slider_value.get())  # but not used here                        

root = tk.Tk()
root.title('Slider_GUI')

frame = TestFrame(root)

# add close function + any commands for when the user hits the 'X'
def close():
    print('Closing')
    # close root window:
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
