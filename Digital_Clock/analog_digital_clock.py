

import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import datetime
from math import *
import os
import time


img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
print (img_path)

class AnalogClock(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.parent = parent

		self.lbl = tk.Label(self,bg='white', bd=20, relief=tk.GROOVE)
		self.lbl.pack()
		
		self.working()
	
	def clock_image(self, hr, min, sec):
		clock = Image.new("RGB", (400, 400), (255, 255, 255)) # ပုံအသစ်လုပ်လိုက်တယ်
		draw = ImageDraw.Draw(clock) # ထိုပုံအသစ်ပေါ််တွင် ရေးဆွဲမည်

		bg = Image.open(img_path + '/' + 'clock.jpg')
		bg = bg.resize((300, 300), Image.ANTIALIAS)
		clock.paste(bg, (50, 50))

		#--------- Drawing hands of hours --------------------
		origin = 200, 200
		
		#======================== Sec Line Images ===================
		draw.line((origin, 200+100*sin(radians(sec)), 200-100*cos(radians(sec))), fill="green", width=3)

		#=== Min Line Images===
		draw.line((origin, 200+80*sin(radians(min)), 200-80*cos(radians(min))), fill="blue", width=3)

		#===Hours Line Images===
		draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="red", width=3)

		# ======================= center ====================
		draw.ellipse((195,195,210, 210), fill="black")

		clock.save("clock_new.png")

	def working(self):
		h = datetime.datetime.now().time().hour
		m = datetime.datetime.now().time().minute
		s = datetime.datetime.now().time().second
		# print (h, m, s)

		hr_ = (h/12)*360
		min_ = (m/60)*360
		sec_ = (s/60)*360

		self.clock_image(hr_, min_, sec_)
		self.img = ImageTk.PhotoImage(file="clock_new.png")
		self.lbl.config(image=self.img)
		self.lbl.after(200, self.working)


class DigitalClock(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.lbl_hr = tk.Label(self, text="12", font=("times new roman", 50, "bold"), bg="#0875B7", fg='white')
		# self.lbl_hr.grid(row=0, column=0, pady=20, padx=20)
		self.lbl_hr.place(x=20, y=5, width=105)

		self.lbl_hr2 = tk.Label(self, text="HOUR", font=("times new roman", 18, "bold"), bg="#0875B7", fg='white', width=8)
		# self.lbl_hr2.grid(row=1, column=0, pady=20, padx=20)
		self.lbl_hr2.place(x=20, y=120, width=105)

		self.lbl_min = tk.Label(self, text="12", font=("times new roman", 50, "bold"), bg="#088EA4", fg='white', width=3)
		# self.lbl_min.grid(row=0, column=1, pady=20, padx=20)
		self.lbl_min.place(x=140, y=5, width=105)

		self.lbl_min2 = tk.Label(self, text="MINUTE", font=("times new roman", 18, "bold"), bg="#088EA4", fg='white', width=8)
		# self.lbl_min2.grid(row=1, column=1, pady=20, padx=20)
		self.lbl_min2.place(x=140, y=120, width=105)

		self.lbl_sec = tk.Label(self, text="12", font=("times new roman", 50, "bold"), bg="#0875B7", fg='white', width=3)
		# self.lbl_sec.grid(row=0, column=2, pady=20, padx=20)
		self.lbl_sec.place(x=260, y=5, width=105)

		self.lbl_sec2= tk.Label(self, text="SECOND", font=("times new roman", 18, "bold"), bg="#0875B7", fg='white', width=8)
		# self.lbl_sec2.grid(row=1, column=2, pady=20, padx=20)
		self.lbl_sec2.place(x=260, y=120, width=105)

		self.lbl_noon = tk.Label(self, text="AM", font=("times new roman", 50, "bold"), bg="#DF002A", fg='white', width=3)
		# self.lbl_noon.grid(row=0, column=3, pady=20, padx=20)
		self.lbl_noon.place(x=380, y=5, width=105)

		self.lbl_noon2= tk.Label(self, text="NOON", font=("times new roman", 20, "bold"), bg="#DF002A", fg='white', width=8)
		# self.lbl_noon2.grid(row=1, column=3, pady=20, padx=20)
		self.lbl_noon2.place(x=380, y=120, width=105)

		self.clock()

	def clock(self):
		h = str(time.strftime("%H"))
		m = str(time.strftime("%M"))
		s = str(time.strftime("%S"))

		# print ("Time module : ",h,m, s)
		if int(h)>12 and int(m)>0:
			self.lbl_noon.config(text='PM')

		if int(h) > 12:
			# h = str(int(h)%12)
			h = str(int(h)-12)
			self.lbl_hr.config(text=h)
		


		self.lbl_min.config(text=m)
		self.lbl_sec.config(text=s)
		self.lbl_hr.config(text=h)

		self.lbl_hr.after(200, self.clock)
	

if __name__ == "__main__":
	root = tk.Tk()
	root = root
	root.title('Anlog Clock')
	root.iconbitmap(img_path + '/' + 'Clock-icon.ico')
	root.geometry("1350x700+0+0")
	root.config(bg="#021e2f") # color of main screen

	analog_clock = AnalogClock(root)
	analog_clock.place(x=80, y=100)

	digital_clock = DigitalClock(root, relief=tk.GROOVE, borderwidth=7)
	digital_clock.place(x=580, y=230, width=530, height=200)
	# digital_clock.config(bg="#021e2f")

	root.mainloop()

