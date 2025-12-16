# Imports from the python standard library:
import os
import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import filedialog
from tkinter import font

class Textbox(tk.LabelFrame):
    def __init__(self,
                 master,
                 label='Textbox frame',
                 hovertip='hovertip',
                 color='black',
                 default_text='entry text',
                 function=None,
                 height=5,
                 width=10,                 
                 row=0,
                 column=0,
                 rowspan=1,
                 columnspan=1,
                 padx=10,
                 pady=5,
                 sticky=None,
                 verbose=False):
        # attributes:
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        tk.LabelFrame.__init__(
            self, self.master, text=self.label, fg=self.color)
        self.grid(row=self.row,
                  column=self.column,
                  rowspan=self.rowspan,
                  columnspan=self.columnspan,
                  sticky=self.sticky,
                  padx=self.padx,
                  pady=self.pady)
        # widget and attribute:
        self.textbox = tk.Text(self, width=self.width, height=self.height)
        self.textbox.grid(padx=self.padx, pady=self.pady)
        self.textbox.insert('1.0', self.default_text)
        self.text = self.textbox.get('1.0','end').strip('\n')
        # bindings:
        if self.hovertip !='hovertip': # target textbox, aviod <Leave> on frame
            self.tip = Hovertip(self.textbox, self.hovertip)
        self.focus_in = tk.BooleanVar()
        self.textbox.bind(                      # user clicks in textbox
            "<FocusIn>", lambda event: self.focus_in.set(1))
        def _leave(event):
            if self.focus_in.get():
                self.update_textbox()
                self.focus_set()
            self.focus_in.set(0)
        self.bind("<Leave>", _leave)            # mouse leaves frame

    def update_textbox(self):
        self.text = self.textbox.get('1.0','end').strip('\n')
        if self.verbose:
            print('%s: text=%s'%(self.label, self.text))
        if self.function is not None:
            self.function(self.text)
        return None

class RadioButtons(tk.LabelFrame):
    def __init__(self,
                 master,
                 label='RadioButtons frame',
                 hovertip='hovertip',
                 color='black',
                 buttons=('button 0','button 1'),
                 default_position=0,
                 function=None,
                 height=3,
                 width=20,
                 row=0,
                 column=0,
                 rowspan=1,
                 columnspan=1,
                 padx=10,
                 pady=5,
                 sticky=None,
                 verbose=False):
        # attributes:
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        tk.LabelFrame.__init__(
            self, self.master, text=self.label, fg=self.color)
        self.grid(row=self.row,
                  column=self.column,
                  rowspan=self.rowspan,
                  columnspan=self.columnspan,
                  sticky=self.sticky,
                  padx=self.padx,
                  pady=self.pady)
        # widgets and attribute:
        self.position = tk.IntVar()
        self.position.set(self.default_position)
        for button in self.buttons:
            self.radiobutton = tk.Radiobutton(
                self,
                text=button,
                value=self.buttons.index(button),
                variable=self.position,
                command=self.update_radiobuttons,
                indicatoron=0,
                height=self.height,
                width=self.width)
            self.radiobutton.grid(
                row=self.buttons.index(button), padx=self.padx, pady=self.pady)
        # bindings:
        if self.hovertip !='hovertip':
            self.tip = Hovertip(self, self.hovertip)

    def update_radiobuttons(self):
        position = self.position.get()
        if self.verbose:
            print('%s: position=%s'%(self.label, position))
        if self.function is not None:
            self.function(position)
        return None

class CheckboxSliderSpinbox(tk.LabelFrame):
    def __init__(self,
                 master,
                 label='CheckboxSliderSpinbox frame',
                 hovertip='hovertip',
                 color='black',
                 orient='horizontal',
                 checkbox_enabled=True,
                 checkbox_default=False,
                 checkbox_function=None,
                 slider_enabled=True,
                 slider_fast_update=False,
                 slider_length=300,
                 tickinterval=4,
                 slider_flipped=False,
                 min_value=0,
                 max_value=100,
                 default_value=0,
                 increment=1,
                 integers_only=True,
                 function=None,
                 row=0,
                 column=0,
                 rowspan=1,
                 columnspan=1,
                 width=10,
                 padx=10,
                 pady=5,
                 sticky=None,
                 show_value=0,
                 verbose=False):
        # attributes:
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        tk.LabelFrame.__init__(
            self, self.master, text=self.label, fg=self.color)
        self.grid(row=self.row,
                  column=self.column,
                  rowspan=self.rowspan,
                  columnspan=self.columnspan,                  
                  sticky=self.sticky,
                  padx=self.padx,
                  pady=self.pady)
        # widgets:
        r, c = (0,0,0), (0,1,2)
        if self.orient == 'vertical': r, c = (0,1,2), (0,0,0)
        if checkbox_enabled:
            self.init_checkbox()
            self.checkbox.grid(
                row=r[0], column=c[0], padx=self.padx, pady=self.pady)
        if slider_enabled:
            self.init_slider()
            self.slider.grid(
                row=r[1], column=c[1], padx=self.padx, pady=self.pady)
        self.init_spinbox()
        self.spinbox.grid(row=r[2], column=c[2], padx=self.padx, pady=self.pady)

    def init_checkbox(self):
        self.checkbox_value = tk.BooleanVar()
        self.checkbox_value.set(self.checkbox_default)
        self.checkbox = tk.Checkbutton(
            self,
            text='On/Off',
            variable=self.checkbox_value,
            command=self.update_checkbox)
        return None

    def update_checkbox(self):
        checkbox_value = self.checkbox_value.get()
        if self.verbose:
            print('%s: checkbox_value=%s'%(self.label, checkbox_value))
        if self.checkbox_function is not None:
            self.checkbox_function(checkbox_value)
        return None

    def init_slider(self):
        self.slider_value = tk.DoubleVar()
        if self.integers_only:
            self.slider_value = tk.IntVar()
        self.slider_value.set(self.default_value)
        command = None
        if self.slider_fast_update:
            command = lambda event: self.update_and_validate(
                self.slider_value.get())
        self.slider = tk.Scale(
            self,
            variable=self.slider_value,
            from_=self.min_value,
            to=self.max_value,
            resolution=self.increment,
            command=command,
            tickinterval=float(
                (self.max_value - self.min_value) / self.tickinterval),
            length=self.slider_length,
            orient=self.orient,
            showvalue=self.show_value)
        if self.slider_flipped:
            self.slider.config(from_=self.max_value, to=self.min_value)
        # bindings:
        self.slider.bind(
            '<ButtonRelease-1>',
            lambda event: self.update_and_validate(self.slider_value.get()))
        return None

    def init_spinbox(self):
        self.spinbox_value = tk.StringVar()
        self.spinbox_value.set(self.default_value)
        self.spinbox = tk.Spinbox(
            self,
            textvariable=self.spinbox_value,
            from_=self.min_value,
            to=self.max_value,
            increment=self.increment,
            command=lambda: self.update_and_validate(None),
            width=self.width,
            justify=tk.CENTER)
        self.value = tk.DoubleVar()
        if self.integers_only:
            self.value = tk.IntVar()
        self.value.set(self.default_value)
        # bindings:
        if self.hovertip !='hovertip': # target spinbox, aviod <Leave> on frame
            self.tip = Hovertip(self.spinbox, self.hovertip)
        self.focus_in = tk.BooleanVar()
        self.spinbox.bind(                      # user clicks in spinbox
            "<FocusIn>", lambda event: self.focus_in.set(1))   
        def _leave(event):
            if self.focus_in.get():
                self.update_and_validate(None)
                self.focus_set()
            self.focus_in.set(0)
        self.bind("<Leave>", _leave)            # mouse leaves frame
        self.spinbox.bind("<Return>", _leave)   # user hits return
        return None

    def update_and_validate(self, value):
        # validate:
        if value is None: # spinbox entry
            value = self.spinbox_value.get()
            if not value.replace("-", "", 1).replace(".", "", 1).isdigit():
                value = self.value.get()# non numeric -> reset to previous
            else: # convert string
                value = float(value)
                if self.integers_only:
                    value = int(value)
        if not self.min_value <= value <= self.max_value:
            value = self.value.get()    # out of range -> reset to previous
        # update:
        self.value.set(value)
        self.spinbox_value.set(value)
        if self.slider_enabled:
            self.slider_value.set(value)
        if self.function is not None:
            self.function(value)
        if self.verbose:
            print('%s: self.value=%s'%(self.label, value))
        return None

class CanvasRectangleSliderTrace2D(tk.Canvas):
    def __init__(self,
                 master,
                 xslider,
                 yslider,
                 row=0,
                 column=0,
                 columnspan=1,
                 color='gray',
                 fill='blue'):
        # attributes:
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        tk.Canvas.__init__(self,
                           self.master,
                           width=self.xslider.slider_length,
                           height=self.yslider.slider_length,
                           bg=self.color)
        self.grid(row=self.row, column=self.column, columnspan=self.columnspan)
        # calculate size:
        self.xdefault = xslider.default_value
        self.ydefault = yslider.default_value        
        self.xlength  = xslider.slider_length
        self.ylength  = yslider.slider_length
        self.xratio   = self.xlength / xslider.max_value
        self.yratio   = self.ylength / yslider.max_value
        x1 = int(round(2 + (self.xlength - self.xdefault * self.xratio) / 2))
        x2 = int(round(1 + (self.xlength + self.xdefault * self.xratio) / 2))
        y1 = int(round(2 + (self.ylength - self.ydefault * self.yratio) / 2))
        y2 = int(round(1 + (self.ylength + self.ydefault * self.yratio) / 2))
        # widgets:
        self.rectangle = self.create_rectangle(x1, y1, x2, y2, fill=self.fill)        
        # bindings:
        self.xslider.slider_value.trace('w', self.update_rectangle)
        self.yslider.slider_value.trace('w', self.update_rectangle)

    def update_rectangle(self, *args):
        if (self.xslider.slider_value.get() == '' or
            self.yslider.slider_value.get() == ''):
            return
        x_width =  int(round(self.xslider.slider_value.get() * self.xratio))
        y_height = int(round(self.yslider.slider_value.get() * self.yratio))
        self.delete(self.rectangle)
        x1 = int(round(2 + (self.xlength - x_width) / 2))
        x2 = int(round(1 + (self.xlength + x_width) / 2))
        y1 = int(round(2 + (self.ylength - y_height) / 2))
        y2 = int(round(1 + (self.ylength + y_height) / 2))
        self.rectangle = self.create_rectangle(x1, y1, x2, y2, fill=self.fill)
        self.grid()
        return None

if __name__=='__main__':
    root = tk.Tk()
    root.title('Root frame title')
    pad = 10

    # Adjust font size:
##    print(font.nametofont('TkDefaultFont').actual())
    size = 10 # default = 9
    font.nametofont("TkDefaultFont").configure(size=size)
    font.nametofont("TkFixedFont").configure(size=size)
    font.nametofont("TkTextFont").configure(size=size)

    # Buttons:
    buttons_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    buttons_frame.grid(row=0, column=0, padx=pad, pady=pad)
    button_width, button_height = 20, 2

    # Hovertips:
    buttons_frame_tip = Hovertip(buttons_frame, "Some tips on buttons!")

    def print_hello():
        print('hello')
        return None
    
    hello_button = tk.Button(
        buttons_frame,
        text="Print 'hello!'",
        command=print_hello,
        width=button_width,
        height=button_height)
    hello_button.grid(row=0, column=0, padx=pad, pady=pad)
    
    # Hovertips on buttons:
    buttons_frame_tip = Hovertip(hello_button, "hello tip!")

    def get_folder_path():
        folder_path = tk.filedialog.askdirectory(
            parent=buttons_frame,
            initialdir=os.getcwd(),
            title='Please choose a folder')
        print('folder_path = %s'%folder_path)
        return None
    
    get_folder_button = tk.Button(
        buttons_frame,
        text="Choose folder",
        command=get_folder_path,
        width=button_width,
        height=button_height)
    get_folder_button.grid(row=1, column=0, padx=pad, pady=pad)

    def get_file_path():
        file_path = tk.filedialog.askopenfilename(
            parent=buttons_frame,
            initialdir=os.getcwd(),
            title='Please choose a file')
        print('file path = %s'%file_path)
        return None
    
    get_file_button = tk.Button(
        buttons_frame,
        text="Choose file",
        command=get_file_path,
        width=button_width,
        height=button_height)
    get_file_button.grid(row=2, column=0, padx=pad, pady=pad)

    def launch_popup_window():
        popup_window = tk.Toplevel()
        popup_window.title('Popup title')
        popup_window.grab_set() # force user to interact with window
        
        # add close function + any commands for when the user hits the 'X'
        def close_popup():
            print('Closing popup')
            popup_window.destroy()
        popup_window.protocol("WM_DELETE_WINDOW", close_popup)
        
        def popup_function():
            print('popup_function')
        popup_button = tk.Button(popup_window, text="popup_function",
                                 command=popup_function,
                                 height=5, width=30)
        popup_button.grid(row=0, column=0, padx=pad, pady=pad)

    launch_popup_button = tk.Button(
        buttons_frame,
        text="Launch popup window",
        command=launch_popup_window,
        width=button_width,
        height=button_height)
    launch_popup_button.grid(row=3, column=0, padx=pad, pady=pad)

    # OptionMenu:
    menu_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    menu_frame.grid(row=0, column=1, padx=pad, pady=pad)
    menu_inner_frame = tk.LabelFrame(menu_frame, text='frame label')
    menu_inner_frame.grid(row=0, column=0, padx=pad, pady=pad)
    def print_option(option):
        print('Option menu selection: %s'%option)
        return None
    options = ('option: A', 'option: B', 'option: C')
    current_choice = tk.StringVar()
    current_choice.set(options[1])
    option_menu = tk.OptionMenu(
        menu_inner_frame, current_choice, *options, command=print_option)
    option_menu.config(width=20, height=2)
    option_menu.grid(row=0, column=0, padx=pad, pady=pad)

    # Textbox:
    text_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    text_frame.grid(row=0, column=2, padx=pad, pady=pad)
    textbox0 = Textbox(text_frame, verbose=True)
    textbox1 = Textbox(
        text_frame,
        label='hello!',
        hovertip='tip!',
        row=1,
        color='blue',
        default_text='testing',
        verbose=True)
    
    # Radiobuttons:
    radio_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    radio_frame.grid(row=0, column=3, padx=pad, pady=pad)
    radiobuttons = RadioButtons(radio_frame, hovertip='tip!', verbose=True)
    
    # CheckboxSliderSpinbox:
    spinbox_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    spinbox_frame.grid(row=1, column=0, padx=pad, pady=pad, columnspan=2)
    checkboxsliderspinbox0 = CheckboxSliderSpinbox(spinbox_frame, verbose=True)
    checkboxsliderspinbox1 = CheckboxSliderSpinbox(
        spinbox_frame,
        label='hello!',
        slider_enabled=False,
        row=1,
        sticky='w',
        color='blue',
        orient='vertical',
        show_value=None,
        verbose=True)
    checkboxsliderspinbox2 = CheckboxSliderSpinbox(
        spinbox_frame,
        checkbox_enabled=False,
        slider_fast_update=True,
        slider_flipped=True,
        min_value=-0.2,
        max_value=1,
        increment=0.1,
        integers_only=False,
        label='span! fast slider!',
        hovertip='tip!',
        row=0,
        column=1,
        rowspan=2,
        color='red',
        orient='vertical',
        verbose=True)

    # CanvasRectangleSliderTrace2D:
    canvas_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    canvas_frame.grid(row=1, column=2, padx=pad, pady=pad, columnspan=2)
    height = CheckboxSliderSpinbox(
        canvas_frame,
        label='height',
        orient='vertical',
        checkbox_enabled=False,
        slider_length=200,
        slider_flipped=True,
        default_value=25,
        row=1,
        verbose=True)
    width = CheckboxSliderSpinbox(
        canvas_frame,
        label='width',
        checkbox_enabled=False,
        default_value=50,
        row=2,
        column=1,
        sticky='s',
        verbose=True)
    CanvasRectangleSliderTrace2D(
        canvas_frame, width, height, row=1, column=1, fill='yellow')

    # add close function + any commands for when the user hits the 'X'
    def close():
        print('Closing')
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", close)
    
    root.mainloop()
