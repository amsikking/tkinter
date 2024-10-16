import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.init_radiobuttons()

    def init_radiobuttons(self):
        self.radiobutton_position=tk.IntVar()
        self.radiobutton_position.set(2)
        
        self.radiobutton1 = tk.Radiobutton(self,
                                           text='Radio button 1',
                                           value=1,
                                           variable=self.radiobutton_position,
                                           command=self.update_radiobutton)        
        self.radiobutton2 = tk.Radiobutton(self,
                                           text='Radio button 2',
                                           value=2,
                                           variable=self.radiobutton_position,
                                           command=self.update_radiobutton)
        self.radiobutton1.grid(row=1)
        self.radiobutton2.grid(row=2)

    def update_radiobutton(self):
        print(self.radiobutton_position.get())

root = tk.Tk()
root.title('Radio_button_GUI')

frame = TestFrame(root)

# add close function + any commands for when the user hits the 'X'
def close():
    print('Closing')
    # close root window:
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
