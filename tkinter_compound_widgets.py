import tkinter as tk
from tkinter import font

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
        self.tk_position=tk.IntVar()
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
        self.rectangle = self.create_rectangle(
            2 + (self.xslider.slider_length -
                 self.xslider.default_value * self.xratio) / 2,
            2 + (self.yslider.slider_length -
                 self.yslider.default_value * self.yratio) / 2,
            2 + (self.xslider.slider_length +
                 self.xslider.default_value * self.xratio) / 2,
            2 + (self.yslider.slider_length +
                 self.yslider.default_value * self.yratio) / 2,
            fill=self.fill)
        return None

    def update_rectangle(self, *args):
        if (self.xslider.tk_slider_value.get() == '' or
            self.yslider.tk_slider_value.get() == ''):
            return
        rectangle_width =  int(
            self.xslider.tk_slider_value.get() * self.xratio)        
        rectangle_height = int(
            self.yslider.tk_slider_value.get() * self.yratio)
        self.delete(self.rectangle)
        self.rectangle = self.create_rectangle(
            2 + (self.xslider.slider_length - rectangle_width) / 2,
            2 + (self.yslider.slider_length - rectangle_height) / 2,
            2 + (self.xslider.slider_length + rectangle_width) / 2,
            2 + (self.yslider.slider_length + rectangle_height) / 2,
            fill='blue')
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
    font.nametofont("TkTextFont").configure(size=size)
    font.nametofont("TkFixedFont").configure(size=size)
    
    # Textbox:
    frame_textbox = tk.LabelFrame(
        root, text='Textbox bounding frame', bd=6)
    frame_textbox0 = Textbox(frame_textbox, verbose=True)
    frame_textbox1 = Textbox(frame_textbox,
                             label='hello!',
                             row=1,
                             color='blue',
                             default_text='testing',
                             verbose=True)
    frame_textbox.grid(row=0, column=0, padx=pad, pady=pad)
    
    # Radiobuttons:
    frame_radiobuttons = tk.LabelFrame(
        root, text='RadioButtons bounding frame', bd=6)
    frame_radiobuttons0 = RadioButtons(frame_radiobuttons, verbose=True)
    frame_radiobuttons.grid(row=1, column=0, padx=pad, pady=pad)
    
    # CheckboxSliderSpinbox:
    frame_checkboxsliderspinbox = tk.LabelFrame(
        root, text='CheckboxSliderSpinbox bounding frame', bd=6)
    frame0 = CheckboxSliderSpinbox(frame_checkboxsliderspinbox, verbose=True)
    frame1 = CheckboxSliderSpinbox(frame_checkboxsliderspinbox,
                                   label='hello!',
                                   slider_enabled=False,
                                   row=1,
                                   sticky='w',
                                   color='blue',
                                   orient='vertical',
                                   show_value=None,
                                   verbose=True)
    frame2 = CheckboxSliderSpinbox(frame_checkboxsliderspinbox,
                                   checkbox_enabled=False,
                                   slider_flipped=True,
                                   label='span!',
                                   row=0,
                                   column=1,
                                   rowspan=2,
                                   color='red',
                                   orient='vertical',
                                   verbose=True)
    frame_checkboxsliderspinbox.grid(row=0, column=2, padx=pad, pady=pad)
    
    # CanvasRectangleSliderTrace2D:
    frame_canvasrectangleslidertrace2d = tk.LabelFrame(
        root, text='CanvasRectangleSliderTrace2D bounding frame', bd=6)    
    height = CheckboxSliderSpinbox(
        frame_canvasrectangleslidertrace2d,
        label='height',
        orient='vertical',
        checkbox_enabled=False,
        slider_flipped=True,
        default_value=25,
        row=1,
        verbose=True)
    width = CheckboxSliderSpinbox(
        frame_canvasrectangleslidertrace2d,
        label='width',
        checkbox_enabled=False,
        default_value=50,
        row=2,
        column=1,
        sticky='s',
        verbose=True)
    CanvasRectangleSliderTrace2D(
            frame_canvasrectangleslidertrace2d, width, height, row=1, column=1)
    frame_canvasrectangleslidertrace2d.grid(row=0, column=3, padx=pad, pady=pad)

    # Quit:
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.grid(row=3, column=2, padx=pad, pady=pad)
    
    root.mainloop()
    root.destroy()
