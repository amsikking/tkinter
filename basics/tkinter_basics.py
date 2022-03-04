import tkinter as tk

# create a root window -> the 'master' for the 'widgets' inside:
root = tk.Tk() 
root.title("This is the root window title") # optional title

# make a label (optional):
label = tk.Label(master=root, text="This is a label")
label.grid(row=0) # display (required), pick location (optional)

# create function for 'click':
def hello():
    print('Hello World!')

# make button to 'click', assign to root window and pass function for command:
button = tk.Button(master=root, text="Click me!", command=hello)
button.grid(row=1)

# make a quit button to exit the event loop and also assign to the root window:
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=2)

# run root window event loop:
root.mainloop()

# close root window:
root.destroy()
