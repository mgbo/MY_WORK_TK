
import tkinter as tk
import math
import time

class Gun:
    def __init__(self):
        self.length = 100 # length of gun
        self.x = 400 # x center position of gun
        self.y = 300 # y center position of gun
        self.id = canvas.create_line(self.x, self.y, self.x+self.length, self.y, width=5, dash='10 2', arrow=tk.LAST)


    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle= (math.atan2(event.y - self.y, event.x - self.x)) # to find slop

        print ("Slop", self.angle)
        # to change position of line
        canvas.coords(self.id, self.x, self.y,
              self.x + self.length * math.cos(self.angle),
              self.y + self.length * math.sin(self.angle)
              )
    
    def targetting_2(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle= (math.atan2(event.y - self.y, event.x - self.x)) # to find slop
        

        # to change position of line
        canvas.coords(self.id, self.x, self.y,
              self.x + self.length * math.cos(self.angle),
              self.y + self.length * math.sin(self.angle)
              )

root = tk.Tk()
root.geometry('800x600')
canvas = tk.Canvas(root, bg='gray80')
canvas.pack(fill=tk.BOTH, expand=1)

gun = Gun()
canvas.bind('<Motion>', gun.targetting)


root.mainloop()

