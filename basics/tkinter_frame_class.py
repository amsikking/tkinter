import tkinter as tk

# create TestFrame class inheriting from tk.Frame (and not tk.Tk)
# we want to create a frame to hang widgets on at this point
# and we don't want to launch a TK (root) window
class TestFrame(tk.Frame):
    # Make __init__ method for our test_frame
    def __init__(self):
        # now also run __init__ method from tk.Frame:
        tk.Frame.__init__(self)
        # i.e. just because we inherited from tk.Frame, doesn't mean we
        # can skip the __init__ method!
        # run object grid method to display frame (inherited from tk.Frame)
        self.grid()
        # run object method to create widgets to hang on frame
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self, text="Click me", command=self.hello)
        self.button.grid(row=1)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(row=2)
        
    def hello(self):
        print("Hello World!")

# Create frame object which has the side effect of creating a root window
# due to the nested tk.Button()
frame = TestFrame()

# run frame object (GUI) event loop (waits for mouse and keyboard events)
frame.mainloop()

frame_parent_name = frame.winfo_parent() # find parent of frame
frame_parent = frame._nametowidget(frame_parent_name) # return parent to python

frame.quit() # exit frame event loop
frame.destroy() # close frame

frame_parent.destroy() # close root window
