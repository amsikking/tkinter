import tkinter as tk

class TestFrame(tk.Frame):
    def __init__(self,
                 master,
                 row,
                 canvas_width,
                 canvas_height,
                 rectangle_width,
                 rectangle_height):
        tk.Frame.__init__(self, master)
        self.grid(row=row)
        
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height
        
        self.init_canvas()
        self.init_rectangle()

    def init_canvas(self):
        self.canvas = tk.Canvas(self,
                                width=self.canvas_width,
                                height=self.canvas_height,
                                bg = 'gray')
        self.canvas.grid()

    def init_rectangle(self):
        left    = (self.canvas_width  - self.rectangle_width)  / 2
        right   = (self.canvas_width  + self.rectangle_width)  / 2
        top     = (self.canvas_height - self.rectangle_height) / 2
        bottom  = (self.canvas_height + self.rectangle_height) / 2
        rectangle = self.canvas.create_rectangle(
            left, top, right, bottom, fill='blue')

root = tk.Tk()
root.title('Canvas_rectangle')

frame1 = TestFrame(root, 0, 500, 200, 200, 100)
frame2 = TestFrame(root, 1, 100, 300, 70, 150)

quit_button = tk.Button(text="Quit", command=root.quit)
quit_button.grid(row=2)

root.mainloop()
root.destroy()
