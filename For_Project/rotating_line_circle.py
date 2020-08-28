
# Formula To Rotate the AntiClock

# end_x = center_x + Line_length * math.cos(angle_in_radians)
# end_y = center_y - Line_length * math.sin(angle_in_radians)

import tkinter as tk
from math import*
from random import *


class Rotate_line:
	list_postion = [(350, 300), (380, 330), (330, 270), (500, 300), (200, 400), (390, 250), (250, 420)]
	def __init__(self, root):

		self.center_x = 300
		self.center_y = 300
		self.angle = 270 # 180 degree is North in my case
		self.l = 250 # Length of the line

		self.c = tk.Canvas(width=600, height=600, bg='black')
		self.c.pack()
		
		# self.c.after(1000, self.rotate)

	def rotate(self):
		self.c.delete(tk.ALL)
		end_x = self.center_x+self.l*sin(radians(self.angle))
		end_y= self.center_y+self.l*cos(radians(self.angle))

		# print (self.center_x, self.center_y, end_x, end_y)


		
		# --- For Cycle -------
		self.c.create_oval(50,50,550,550, outline='green', width=3, fill='blue')
		self.c.create_oval(100,100,500,500, outline='green', width=3, fill='blue')
		self.c.create_oval(150, 150, 450, 450, outline='green', width=3,  fill='blue')
		self.c.create_oval(250, 250, 350, 350, outline='green', width=3, fill='blue')

		# ---- X axis and Y axis -----------------
		self.line = self.c.create_line(50, 300, 550, 300, fill='darkgreen', width=3, dash='10 2')
		self.line = self.c.create_line(300, 50, 300, 550, fill='darkgreen', width=3, dash='10 2')


		# ------ For position of ship ------------
		# self.c.create_text(300, 300, text="O", justify=tk.CENTER, font="Verdana 20", fill="yellow")
		# for _ in range(3):
		# 	p = choice(Rotate_line.list_postion)
		# 	# dx = randint(20, 100)
		# 	# x = int(p[0]) + dx
		# 	# y = int(p[1]) + dx
		# 	self.c.create_text(p, text="∆", justify=tk.CENTER, font="Verdana 20", fill="red")
		# 	# self.c.create_text(choice(Rotate_line.list_postion), text="∆", justify=tk.CENTER, font="Verdana 20", fill="red")

		self.c.create_text(400, 300-2, text="o", justify=tk.CENTER, font="Verdana 20", fill="red")

		# ----- Rotation line -------
		self.line = self.c.create_line(self.center_x, self.center_y, \
			(self.center_x+self.l*cos(radians(self.angle))), \
			(self.center_y+self.l*sin(radians(self.angle))), fill="yellow", width=3)
		

		self.angle += 3
		if (self.angle > 360):
			self.angle = self.angle - 360
		
		# n = int(input("n :"))
		self.c.after(100, self.rotate) # speed of screen


def angle_ship(x_cen=300, y_cen=300, x_other=400, y_other=300):
		dx = abs(x_other - x_cen)
		dy = abs(y_other - y_cen)
		print (dx,dy)
		if dx!=0:
			m = dy/dx	
			# print (m)
			radians_pos = atan(m)
			degree = degrees(radians_pos)

			if x_cen < x_other and y_cen>y_other:
				print ("degree 1 :", degree)

			elif x_cen > x_other and y_cen> y_other:
				degree = 180 - degree
				print ('degree 2', degree)

			elif x_cen > x_other and y_cen < y_other:
				degree = 270 - degree
				print ('degree 3', degree)

			elif x_cen < x_other and y_cen < y_other:
				degree = 360 - degree
				print ('degree 4', degree)

			elif x_cen > x_other and y_cen == y_other:
				degree = 180
				print (degree)

			elif x_cen< x_other and y_cen == y_other:
				degree = 360
				print (degree)

		elif x_cen == x_other and y_other>y_cen:
				degree = 270
				print ('degree 5', degree)

		elif x_cen == x_other and y_other<y_cen:
				degree = 90
				print ('degree 6', degree)



if __name__ == "__main__":
	root = tk.Tk()
	line = Rotate_line(root)
	line.rotate()
	
	frame_1 = tk.Frame(root)
	frame_1.pack()


	l = tk.Label(frame_1, text='Hello', font=("time new roman", 25, 'bold'))
	l.pack()
	
	angle_ship()
	root.mainloop()










