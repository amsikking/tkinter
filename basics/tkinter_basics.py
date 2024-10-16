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

# add close function + any commands for when the user hits the 'X'
def close():
    print('Closing')
    # close root window:
    root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# run root window event loop:
root.mainloop()
