import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self,
                 master,
                 canvas_width,
                 canvas_height):
        tk.Frame.__init__(self, master)
        self.grid()
        
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.init_canvas()
        self.init_rectangle()
        self.init_slider()

    def init_canvas(self):
        self.canvas = tk.Canvas(self,
                                width=self.canvas_width,
                                height=self.canvas_height,
                                bg = 'gray')
        self.canvas.grid(row=0)

    def init_rectangle(self):
        self.rectangle = self.canvas.create_rectangle(0, 0, 0, 0, fill='blue')

    def init_slider(self):
        self.slider_value = tk.IntVar()
        self.slider = tk.Scale(self,
                               command=self.print_and_update,
                               orient='horizontal',
                               length=self.canvas_width,
                               variable=self.slider_value)
        self.slider.grid(row=1)

    def print_and_update(self, scale_value):    # scale_value required
        print(self.slider_value.get())          # but not used here
        self.canvas.delete(self.rectangle)
        rectangle_width = (self.slider_value.get() * self.canvas_width) / 100
        rectangle_height = self.canvas_height
        left    = (self.canvas_width  - rectangle_width)  / 2
        right   = (self.canvas_width  + rectangle_width)  / 2
        top     = (self.canvas_height - rectangle_height) / 2
        bottom  = (self.canvas_height + rectangle_height) / 2
        self.rectangle = self.canvas.create_rectangle(
            left, top, right, bottom, fill='blue')

root = tk.Tk()
root.title('Canvas_rectangle_slider')

frame = TestFrame(root, 300, 50)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=2)

root.mainloop()
root.destroy()
