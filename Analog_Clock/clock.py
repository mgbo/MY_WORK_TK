
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import datetime
import time
from math import*

class Clcok:
	def __init__(self, root):
		self.root = root
		self.root.title('Anlog Clock')
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="#021e2f") # color of main screen

		title = tk.Label(self.root, text="Tkinter Analog Clock", font=("times new roman", \
		 50, "bold"), bg="#04444a", fg='white').place(x=0, y=50, relwidth=1)

		self.lbl = tk.Label(self.root, bg="white", bd=20, relief=tk.GROOVE)
		self.lbl.place(x=450, y=150, height=400, width=400)
		# self.clock_image(hr_, min_, sec_)
		self.working()

	def clock_image(self, hr_, min_, sec_):
		clock = Image.new("RGB", (400, 400), (255, 255, 255))
		draw = ImageDraw.Draw(clock) # for drawing on the image

		#===For Clock Image
		bg = Image.open('clock.jpg')
		bg = bg.resize((300, 300), Image.ANTIALIAS)
		clock.paste(bg, (50, 50))
		# clock.save("clock_new.jpg")


		# Formula To Rotate the AntiClock
		# angle_in_radians = angle_in_degrees * math.pi / 180
		# Line_length = 100
		# center_x = 250
		# center_y = 250
		# end_x = center_x + Line_length * math.cos(angle_in_radians)
		# end_y = center_y - Line_length * math.sin(angle_in_radians)
		

		#--------- Drawing hands of hours --------------------
		origin = 200, 200
		
		#===Hours Line Images===
		draw.line((origin, 200+50*sin(radians(hr_)), 200-50*cos(radians(hr_))), fill="red", width=3)

		#===Min Line Images===
		draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="blue", width=3)

		#===Sec Line Images===
		draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="green", width=3)

		# center
		draw.ellipse((195,195,210, 210), fill="black")

		clock.save("clock_new.png")

	def working(self):
		h = datetime.datetime.now().time().hour
		m = datetime.datetime.now().time().minute
		s = datetime.datetime.now().time().second

		hr_ = (h/12)*360
		min_ = (m/60)*360
		sec_ = (s/60)*360

		# print (h, m, s)
		# print (hr_, min_, sec_)

		self.clock_image(hr_, min_, sec_)
		self.img = ImageTk.PhotoImage(file="clock_new.png")
		self.lbl.config(image=self.img)
		self.lbl.after(200, self.working)


if __name__ == "__main__":
	root = tk.Tk()
	obj = Clcok(root)
	root.mainloop()








