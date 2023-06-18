import os
import tkinter as tk
from tkinter import font
from tkinter import filedialog

class Textbox(tk.LabelFrame):
    def __init__(self,
                 master,
                 label='Textbox frame',
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
                 pady=10,
                 sticky=None,
                 verbose=False):
        tk.LabelFrame.__init__(self, master, text=label, fg=color)
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        self.grid(row=self.row,
                  column=self.column,
                  rowspan=self.rowspan,
                  columnspan=self.columnspan,
                  sticky=self.sticky,
                  padx=self.padx,
                  pady=self.pady)
        # widgets:
        self.init_textbox()
        self.text = self.textbox.get('1.0','end').strip('\n')

    def init_textbox(self):
        self.textbox = tk.Text(self, width=self.width, height=self.height)
        self.textbox.insert('1.0', self.default_text)
        self.textbox.bind("<Return>", self.update_textbox)
        self.textbox.bind("<FocusOut>", self.update_textbox)
        self.textbox.grid(padx=self.padx, pady=self.pady)
        return None

    def update_textbox(self, event): # event is not used here (.bind)
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
                 pady=10,
                 sticky=None,
                 verbose=False):
        tk.LabelFrame.__init__(self, master, text=label, fg=color)
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        self.grid(row=self.row,
                  column=self.column,
                  rowspan=self.rowspan,
                  columnspan=self.columnspan,
                  sticky=self.sticky,
                  padx=self.padx,
                  pady=self.pady)
        # widgets:
        self.init_radiobuttons()
        self.position = self.tk_position.get()

    def init_radiobuttons(self):
        self.tk_position = tk.IntVar()
        self.tk_position.set(self.default_position)
        for button in self.buttons:
            self.radiobutton = tk.Radiobutton(
                self,
                text=button,
                value=self.buttons.index(button),
                variable=self.tk_position,
                command=self.update_radiobuttons,
                indicatoron=0,
                height=self.height,
                width=self.width)
            self.radiobutton.grid(
                row=self.buttons.index(button),
                padx=self.padx,
                pady=self.pady)
        return None

    def update_radiobuttons(self):
        self.position = self.tk_position.get()
        if self.verbose:
            print('%s: position=%s'%(self.label, self.position))
        if self.function is not None:
            self.function(self.position)
        return None

class CheckboxSliderSpinbox(tk.LabelFrame):
    def __init__(self,
                 master,
                 label='CheckboxSliderSpinbox frame',
                 color='black',
                 orient='horizontal',
                 checkbox_enabled=True,
                 checkbox_default=False,
                 checkbox_function=None,
                 slider_enabled=True,
                 slider_length=300,
                 tickinterval=4,
                 slider_flipped=False,
                 min_value=0,
                 max_value=100,
                 default_value=0,
                 function=None,
                 row=0,
                 column=0,
                 rowspan=1,
                 columnspan=1,
                 width=10,
                 padx=10,
                 pady=10,
                 sticky=None,
                 show_value=0,
                 verbose=False):
        tk.LabelFrame.__init__(self, master, text=label, fg=color)
        args = locals()
        args.pop('self')
        for k, v in args.items(): setattr(self, k, v)
        # frame:
        self.grid(row=self.row,
                  column=self.column,
                  rowspan=self.rowspan,
                  columnspan=self.columnspan,                  
                  sticky=self.sticky,
                  padx=self.padx,
                  pady=self.pady)
        if checkbox_enabled: self.init_checkbox()
        if slider_enabled: self.init_slider()
        self.init_spinbox()
        # widgets:
        r, c = (0,0,0), (0,1,2)
        if self.orient == 'vertical': r, c = (0,1,2), (0,0,0)
        if checkbox_enabled:
            self.checkbox.grid(
                row=r[0], column=c[0], padx=self.padx, pady=self.pady)
        if slider_enabled:
            self.slider.grid(
                row=r[1], column=c[1], padx=self.padx, pady=self.pady)
        self.spinbox.grid(row=r[2], column=c[2], padx=self.padx, pady=self.pady)

    def init_checkbox(self):
        self.tk_checkbox_value = tk.BooleanVar()
        self.tk_checkbox_value.set(self.checkbox_default)
        self.checkbox = tk.Checkbutton(
            self,
            text='On/Off',
            variable=self.tk_checkbox_value,
            command=self.update_checkbox)
        self.checkbox_value = self.tk_checkbox_value.get()
        return None

    def update_checkbox(self):
        self.checkbox_value = self.tk_checkbox_value.get()
        if self.verbose:
            print('%s: checkbox_value=%s'%(self.label, self.checkbox_value))
        if self.checkbox_function is not None:
            self.checkbox_function(self.checkbox_value)
        return None
 
    def init_slider(self):        
        self.tk_slider_value = tk.IntVar()
        self.tk_slider_value.set(self.default_value)
        self.slider = tk.Scale(
            self,
            variable=self.tk_slider_value,
            from_=self.min_value,
            to=self.max_value,
            command=self.update_slider,
            tickinterval=int(
                (self.max_value - self.min_value) / self.tickinterval),
            length=self.slider_length,
            orient=self.orient,
            showvalue=self.show_value)
        self.slider_value = self.tk_slider_value.get()
        if self.slider_flipped:
            self.slider.config(from_=self.max_value, to=self.min_value)
        return None

    def update_slider(self, scale_value): # scale_value not used here (.Scale)
        self.slider_value = self.tk_slider_value.get()
        if self.verbose:
            print('%s: slider_value=%s'%(self.label, self.slider_value))
        if self.function is not None:
            self.function(self.slider_value)
        self.tk_spinbox_value.set(self.slider_value)
        self.spinbox_value = self.slider_value
        return None

    def init_spinbox(self):
        self.tk_spinbox_value = tk.StringVar()
        self.tk_spinbox_value.set(self.default_value)
        self.spinbox = tk.Spinbox(
            self,
            textvariable=self.tk_spinbox_value,
            from_=self.min_value,
            to=self.max_value,
            command=self.update_spinbox,
            width=self.width,
            justify=tk.CENTER)
        self.spinbox.bind("<Return>", self.update_spinbox_and_validate)
        self.spinbox.bind("<FocusOut>", self.update_spinbox_and_validate)
        self.spinbox_value = int(self.tk_spinbox_value.get())
        return None

    def update_spinbox(self):
        self.update_spinbox_and_validate(None)
        return None

    def update_spinbox_and_validate(self, event): # event not used here (.bind)
        spinbox_value = self.tk_spinbox_value.get()
        if (not spinbox_value.isdigit() or
            int(spinbox_value) < self.min_value or
            int(spinbox_value) > self.max_value):
            self.tk_spinbox_value.set(self.spinbox_value)
        self.spinbox_value = int(self.tk_spinbox_value.get())
        if self.slider_enabled:
            self.tk_slider_value.set(self.spinbox_value)
        if self.verbose:
            print('%s: spinbox_value=%s'%(self.label, self.spinbox_value))
        if self.function is not None:
            self.function(self.spinbox_value)
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
        tk.Canvas.__init__(self,
                           master,
                           width=xslider.slider_length,
                           height=yslider.slider_length,
                           bg=color)
        self.master = master
        self.xslider = xslider
        self.yslider = yslider
        self.fill = fill
        self.xratio = xslider.slider_length / xslider.max_value
        self.yratio = yslider.slider_length / yslider.max_value
        self.grid(row=row, column=column, columnspan=columnspan)
        self.init_rectangle()
        self.xslider.tk_slider_value.trace('w', self.update_rectangle)
        self.yslider.tk_slider_value.trace('w', self.update_rectangle)

    def init_rectangle(self):
        x1 = int(round(2 + (self.xslider.slider_length -
                            self.xslider.default_value * self.xratio) / 2))
        x2 = int(round(1 + (self.xslider.slider_length +
                            self.xslider.default_value * self.xratio) / 2))
        y1 = int(round(2 + (self.yslider.slider_length -
                            self.yslider.default_value * self.yratio) / 2))
        y2 = int(round(1 + (self.yslider.slider_length +
                            self.yslider.default_value * self.yratio) / 2))
        self.rectangle = self.create_rectangle(x1, y1, x2, y2, fill=self.fill)
        return None

    def update_rectangle(self, *args):
        if (self.xslider.tk_slider_value.get() == '' or
            self.yslider.tk_slider_value.get() == ''):
            return
        x_width =  int(round(self.xslider.tk_slider_value.get() * self.xratio))
        y_height = int(round(self.yslider.tk_slider_value.get() * self.yratio))
        self.delete(self.rectangle)
        x1 = int(round(2 + (self.xslider.slider_length - x_width) / 2))
        x2 = int(round(1 + (self.xslider.slider_length + x_width) / 2))
        y1 = int(round(2 + (self.yslider.slider_length - y_height) / 2))
        y2 = int(round(1 + (self.yslider.slider_length + y_height) / 2))
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

    def print_hello():
        print('hello')
        return None

    def get_folder_path():
        folder_path = tk.filedialog.askdirectory(
            parent=buttons_frame,
            initialdir=os.getcwd(),
            title='Please choose a folder')
        print('folder_path = %s'%folder_path)
        return None

    def get_file_path():
        file_path = tk.filedialog.askopenfilename(
            parent=buttons_frame,
            initialdir=os.getcwd(),
            title='Please choose a file')
        print('file path = %s'%file_path)
        return None
    
    hello_button = tk.Button(
        buttons_frame,
        text="Print 'hello!'",
        command=print_hello,
        width=button_width,
        height=button_height)
    hello_button.grid(row=0, column=0, padx=10, pady=10)

    get_folder_button = tk.Button(
        buttons_frame,
        text="Choose folder",
        command=get_folder_path,
        width=button_width,
        height=button_height)
    get_folder_button.grid(row=1, column=0, padx=10, pady=10)

    get_file_button = tk.Button(
        buttons_frame,
        text="Choose file",
        command=get_file_path,
        width=button_width,
        height=button_height)
    get_file_button.grid(row=2, column=0, padx=10, pady=10)

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
    option_menu.grid(row=0, column=0, padx=10, pady=10)

    # Textbox:
    text_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    text_frame.grid(row=0, column=2, padx=pad, pady=pad)
    textbox0 = Textbox(text_frame, verbose=True)
    textbox1 = Textbox(
        text_frame,
        label='hello!',
        row=1,
        color='blue',
        default_text='testing',
        verbose=True)
    
    # Radiobuttons:
    radio_frame = tk.LabelFrame(root, text='BOUNDING FRAME', bd=6)
    radio_frame.grid(row=0, column=3, padx=pad, pady=pad)
    radiobuttons = RadioButtons(radio_frame, verbose=True)
    
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
        slider_flipped=True,
        label='span!',
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

    # Quit:
    quit_button = tk.Button(
        root, text="Quit", command=root.quit, height=5, width=30)
    quit_button.grid(row=1, column=4, padx=pad, pady=pad)
    
    root.mainloop()
    root.destroy()
