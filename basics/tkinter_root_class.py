import tkinter as tk

class Gui(tk.Frame):
    def __init__(self):
        # pack root code into __init__ and then simply call the Gui class
        self.root = tk.Tk()
        self.root.title('Root_window, single frame')
        # we inherited from tk.Frame, but we still need to run the __init__
        # method and pass in the root as master
        tk.Frame.__init__(self, self.root)
        self.grid()
    
        self.buttons()

        # add close function + any commands for when the user hits the 'X'
        def close():
            print('Closing')
            # close root window:
            self.root.destroy()
        self.root.protocol("WM_DELETE_WINDOW", close)
        
        self.root.mainloop()
        
    def buttons(self): # let the frame be the master, it could also be the root
        self.print_button = tk.Button(
            self, text="Print", command=self.print)
        self.print_button.grid(row=0)
        
        self.quit_button = tk.Button(
            self, text="Quit_frame", command=self.destroy)
        self.quit_button.grid(row=1)

    def print(self):
        print('hello')

gui = Gui()
