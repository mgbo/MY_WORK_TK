
import tkinter as tk
from random import randint
import math

WIDTH = 600
HEIGHT = 600

class Circle:
    def __init__(self, x, y, R=10, color=None):
        self.x = x
        self.y = y
        self.R = R
        self.color = color
        self.circle_id = canvas.create_oval(self.x +self.R, self.y +self.R, \
                                        self.x - self.R, self.y - self.R, outline='white', width=1, fill=self.color)
    
    def variable_range_marker(self, event):
        canvas.delete(self.circle_id)
        x_2, y_2 = event.x, event.y

        d = math.sqrt((x_2-self.x)**2 + (y_2 - self.y)**2)
        print ("({},{}), ({},{}) --> {}".format(self.x, self.y, x_2, y_2, d))

        self.circle_id = canvas.create_oval(self.x-d, self.y-d, self.x+d, self.y+d, outline='red')


    def button_variable_range_marker(self, event):
        # canvas.delete(self.circle_id)
        x_2, y_2 = event.x, event.y

        d = math.sqrt((x_2-self.x)**2 + (y_2 - self.y)**2)
        print ("Button : ({},{}), ({},{}) --> {}".format(self.x, self.y, x_2, y_2, d))

        self.circle_id = canvas.create_oval(self.x-d, self.y-d, self.x+d, self.y+d, outline='red')
    

class XY_axis:
    def __init__(self, start_x, start_y, finish_x, finish_y):
        self.start_x = start_x
        self.start_y = start_y
        self.finish_x = finish_x
        self.finish_y = finish_y
        self.axis = canvas.create_line(self.start_x, self.start_y, self.finish_x, self.finish_y, width=2, fill='white')


if __name__ == "__main__":

    root = tk.Tk()
    root.geometry(str(WIDTH)+'x'+str(HEIGHT))

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
    canvas.pack()

    x_center = 300
    y_center = 300

    c = Circle(x_center,y_center, 150, 'blue')
    print (c.circle_id)

    c2 = Circle(x_center, y_center, 100, 'blue')
    print (c2.circle_id)

    # ----------- XY axis --------------------
    x_axis = XY_axis(150, 300, 450, 300)
    y_axis = XY_axis(300, 150, 300, 450)


    crm = Circle(x_center, y_center, 30)
    print ("Circle number is : ",crm.circle_id)

    canvas.bind("<Motion>",  crm.variable_range_marker)
    canvas.bind("<ButtonRelease-1>", crm.button_variable_range_marker)
    


    root.mainloop()

