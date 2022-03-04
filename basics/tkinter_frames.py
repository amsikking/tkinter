import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self, master, label, row):
        tk.Frame.__init__(self, master)
        self.label = label
        self.grid(row=row)
        self.buttons()

    def buttons(self):
        # because 'self' is passed as master these belong to each frame
        self.print_button = tk.Button(
            self, text=self.label, command=self.print)
        self.print_button.grid(row=0)
        
        self.quit_button = tk.Button(
            self, text="Quit_frame", command=self.destroy)
        self.quit_button.grid(row=1)

    def print(self):
        print(self.label, 'hello')

root = tk.Tk()
root.title('Multiple_frames')

frame1 = TestFrame(root, 'Print1', 2) # pack multiple frames in a window
frame2 = TestFrame(root, 'Print2', 1)

# 'quit' command is for exiting the main event loop which belongs to root:
quit_root_button = tk.Button(root, text="Quit_root", command=root.quit)
quit_root_button.grid()

root.mainloop()
root.destroy()
