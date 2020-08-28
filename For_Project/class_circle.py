
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
        x_2, y_2 = event.x, event.y

        d = math.sqrt((x_2-self.x)**2 + (y_2 - self.y)**2)
        print ("({},{}), ({},{}) --> {}".format(self.x, self.y, x_2, y_2, d))


class XY_axis:
    def __init__(self, start_x, start_y, finish_x, finish_y):
        self.start_x = start_x
        self.start_y = start_y
        self.finish_x = finish_x
        self.finish_y = finish_y
        self.axis = canvas.create_line(self.start_x, self.start_y, self.finish_x, self.finish_y, width=2, fill='white')



class Text:
    def __init__(self, x, y,text):
        self.x = x
        self.y = y
        self.text = text
        self.text_id = canvas.create_text(self.x, self.y, text=self.text, fill='white')


class Circle_degree:
    def __init__(self, x, y, R, angle):
        self.x = x
        self.y = y
        self.R = R
        self.angle = angle
        self.name_degree()


    def name_degree(self):
        for i in range(36):
            self.angle += 10
            x1 = self.x+self.R*math.sin(math.radians(self.angle))
            y1 = self.y+self.R*math.cos(math.radians(self.angle))

            canvas.create_line(x1, y1, x1, y1-5, fill='red', width=2)
            print (f"({x1},{y1}), ({x1},{x1-5})")
        


class Heading_line:
    def __init__(self, center_x, center_y, l):
        self.angle = 0
        self.center_x = center_x
        self.center_y = center_y
        self.l = l + 11

        self.line = canvas.create_line(self.center_x, self.center_y, \
            (self.center_x+self.l*math.cos(math.radians(self.angle))), \
            (self.center_y+self.l*math.sin(math.radians(self.angle))), fill='red', width=2, arrow=tk.LAST)
    
    def rotate_right_heading_line(self, event):
        print (event.keysym)
        canvas.delete(self.line)
        self.angle += 2
        self.line = canvas.create_line(self.center_x, self.center_y, \
            (self.center_x+self.l*math.cos(math.radians(self.angle))), \
            (self.center_y+self.l*math.sin(math.radians(self.angle))), fill='red', width=2, arrow=tk.LAST)
        if (self.angle > 360):
            self.angle = self.angle - 360

    def rotate_left_heading_line(self, event):
        print (event.keysym)
        canvas.delete(self.line)
        self.angle -= 2
        self.line = canvas.create_line(self.center_x, self.center_y, \
            (self.center_x+self.l*math.cos(math.radians(self.angle))), \
            (self.center_y+self.l*math.sin(math.radians(self.angle))), fill='red', width=3, arrow=tk.LAST)
        if (self.angle > 360):
            self.angle = self.angle - 360


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

    # ------------- name of degree ----------------
    t1 = Text(x_center+150+10, y_center, '90')
    t2 = Text(x_center-160-10, y_center, '270')
    t3 = Text(x_center, y_center+150+10, '180')
    t4 = Text(x_center, y_center-150-10, '360')

    # ------ mark of degree in circle -------------
    l1 = Circle_degree(300, 300, 150, 10)

    # ---  show heading line while move ship ----------------
    line_heading = Heading_line(300, 300, 150)
    root.bind("<KeyPress-Right>", lambda e: line_heading.rotate_right_heading_line(e))
    root.bind("<KeyPress-Left>", lambda e: line_heading.rotate_left_heading_line(e))


    crm = Circle(x_center, y_center, 30)
    print ("Circle number is : ",crm.circle_id)
    root.bind("<Motion>", lambda e: crm.variable_range_marker(e))


    root.mainloop()

