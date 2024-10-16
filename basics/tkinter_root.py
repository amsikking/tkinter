# root framework using a class, builds on tkinter_frame_class
import tkinter as tk

class TestFrame(tk.Frame):
    # Initialize frame with master variable so it will require a master or
    # parent object to run (like a root window) 
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # set .master attribute so we can pass this to the tk. objects
        self.master = master
        self.grid()
        self.create_buttons()

    def create_buttons(self):
        # because 'self.master' is passed as master these belong to the root
        self.button = tk.Button(
            self.master, text="Click me", command=self.hello)
        self.button.grid(row=1)
        
    def hello(self):
        print("Hello World!")

# create a root window, add a title and set size
root = tk.Tk()
root.title("This is the root window")

# Create frame object and set master to root window
frame = TestFrame(root)

# add close function + any commands for when the user hits the 'X'
def close():
    print('Closing')
    # close root window:
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# run frame event loop (waits for mouse and keyboard events)
root.mainloop()
