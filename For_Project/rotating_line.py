
# origin = 200, 200

# #===Hours Line Images===
# draw.line((origin, 200+50*sin(radians(hr_)), 200-50*cos(radians(hr_))), fill="red", width=3)

# #===Min Line Images===
# draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="blue", width=3)

# #===Sec Line Images===
# draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="green", width=3)

# Formula To Rotate the AntiClock
# angle_in_radians = angle_in_degrees * math.pi / 180
# Line_length = 100
# center_x = 250
# center_y = 250
# end_x = center_x + Line_length * math.cos(angle_in_radians)
# end_y = center_y - Line_length * math.sin(angle_in_radians)


# newx = ((x2-x1)*math.cos(angle)-(y2-y1)*math.sin(angle)) + x1
# newy = ((x2-x1)*math.sin(angle)+(y2-y1)*math.cos(angle)) + y1


import tkinter as tk
from math import*

class Rotate_line:

	def __init__(self, root):

		self.center_x = 300
		self.center_y = 300
		self.angle = 180
		self.l = 200 # Length of the line

		self.c = tk.Canvas(width=600, height=600, bg='black')
		self.c.pack()

		# self.c.after(1000, self.rotate)
		
	
	def rotate(self):
		self.c.delete(tk.ALL)
		end_x = self.center_x+self.l*sin(radians(self.angle))
		end_y= self.center_y+self.l*cos(radians(self.angle))

		# print (self.center_x, self.center_y, end_x, end_y)

		self.line = self.c.create_line(self.center_x, self.center_y, \
			(self.center_x+self.l*sin(radians(self.angle))), \
			(self.center_y+self.l*cos(radians(self.angle))), fill="green", width=3, arrow=tk.LAST)

		self.angle += 3
		if (self.angle > 360):
			self.angle = self.angle - 360
		
		# n = int(input('input --> :'))
		
		self.c.after(60, self.rotate)


if __name__ == "__main__":
	root = tk.Tk()
	line = Rotate_line(root)
	line.rotate()
	
	
	root.mainloop()










