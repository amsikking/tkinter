import tkinter as tk

# create function for 'click':
def hello():
    print('Hello World!')

# make a 'click' button, which in the absence of a master,
# also launches a root window and starts an event loop!
click_button = tk.Button(text="Click me!", command=hello)
click_button.grid(row=1)

parent_name = click_button.winfo_parent() # find parent of button object
parent = click_button._nametowidget(parent_name) # return parent to python

##eventloop_name = click_button._winfo_mainloop()

# make a quit button to exit the event loop
# this lands in the root window but it would better to set 'master=parent'
# use parent to destory root window
quit_button = tk.Button(text="Quit", command=parent.destroy)
quit_button.grid(row=2)

# note that the program finishes but the button persists
print('finished')
# this is usually not a great way to use tkinter...
