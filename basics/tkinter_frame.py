import tkinter as tk

# create a frame, which also creates a root window (parent)
frame = tk.Frame()
frame.grid() # add the frame to the display grid

# create command function for 'click'
def hello():
    print('Hello World!')

# make a 'click' button with frame as 'master'
button = tk.Button(master=frame, text="Click me!", command=hello)
button.grid(row=1)

# make a quit button to exit the event loop
quit_button = tk.Button(frame, text="Quit", command=frame.quit)
quit_button.grid(row=2)

# run root window event loop
frame.mainloop()

# important: the 'quit' cmd exits the mainloop (if it's running)
# otherwise it does nothing
# 'destroy' kills the widgets or main window regardless of the mainloop

# optional extra
# find parent of frame object (root window) before destroying the frame
# this is not created by tk.Frame, but tk.Frame is the master of tk.Button
# tk.Button, even with frame as master, will create a root window it seems
##parent_name = frame.winfo_parent()
# now return parent object to python
##parent = frame._nametowidget(parent_name)

# destroy frame
frame.destroy()

# can now use the parent object we found this to close the root window
##parent.destroy()
