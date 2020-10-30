
import matplotlib
# matplotlib.use("TkAgg")
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from itertools import count
import random

import tkinter as tk
from  tkinter import ttk

import os

LARGE_FONT = ("Verdana", 12)
# style.use("ggplot")



f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


x_vals = []
y_vals = []
index = count()
# print(next(index))

# data = np.array([])
cond = False

def animate(i):
	# x_vals.append(next(index))
	d = random.randint(10,25)
	x = next(index)
	x_vals.append(x)
	y_vals.append(d)
	# print (d)
	print(x)


	a.clear()
	a.set_xlabel('X data')
	a.set_ylabel('Pressure')
	# a.grid(color="blue", which="both", linestyle=':', linewidth=5)
	a.grid()
	a.set_xlim(left=max(0, x-50), right=i+50)
	a.set_ylim(0, 30)
	a.plot(x_vals, y_vals) # 'ro'


loc_img = os.path.abspath(os.path.join(os.path.dirname(__file__),'ship.ico'))
print (loc_img)



class SeaofBTCapp(tk.Tk):
	def __init__(self, *arg, **kwargs):
		tk.Tk.__init__(self, *arg, **kwargs)
		# super().__init__(self, *arg, **kwargs)
		# tk.Tk.iconbitmap(self, default='ship.ico')
		# tk.Tk.wm_title(self, "sea of BTC client")
		self.geometry("800x700")
		self.resizable(False, False)

		containter = tk.Frame(self)
		containter.pack(side='top', fill='both', expand=True)
		containter.grid_rowconfigure(0, weight=1)
		containter.grid_columnconfigure(0, weight=1)

		self.frames = {}
		# frame = StartPage(containter, self)
		# self.frames[StartPage] = frame
		# frame.grid(row=0, column=0, sticky="nsew")
		# self.show_frame(StartPage)

		for F in (StartPage, PageOne, PageTwo, PageThree):
			# print (F, type(F))
			frame = F(containter, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
			self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise() # လေ့လာရန်

	def quit(self):
		self.destroy()


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Start Page', bg='#ffb3fe', fg='green', font=LARGE_FONT)
		label.pack(pady=10, padx=10, fill='x')

		button_q = ttk.Button(self, text='Quit', width='15', command=lambda: parent.quit())
		button_q.pack()

		button = ttk.Button(self, text='Visti Page 1', width='15', command=lambda: controller.show_frame(PageOne))
		button.pack()


		button2 = ttk.Button(self, text='Visti Page 2', width='15', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text='Graph Page', width='15', command=lambda: controller.show_frame(PageThree))
		button3.pack()

		label_1 = tk.Label(self, text='ပထမ စာမျက်နှာမှကြိုဆိုပါတယ်', fg='green', font=LARGE_FONT)
		label_1.place(x=350, y=320)



class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.config(bg='grey')

		label = tk.Label(self, text='Page One!!', bg='green', font=LARGE_FONT)
		label.pack(pady=10, padx=10, fill='x')

		button1 = ttk.Button(self, text='Back to Home', width='15', command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text='Back to Page Two', width='15', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text='Back to Graph Page', width='15', command=lambda: controller.show_frame(PageThree))
		button3.pack()

class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Page Two!!', bg='red', font=LARGE_FONT)
		label.pack(pady=10, padx=10, fill='x')

		button1 = ttk.Button(self, text='Back to Home', width='15', command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text='Back to PageOne', width='15', command=lambda: controller.show_frame(PageOne))
		button2.pack()

		button3 = ttk.Button(self, text='Back to Graph Page', width='15', command=lambda: controller.show_frame(PageThree))
		button3.pack()

class PageThree(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Graph Page!!', bg='blue', font=LARGE_FONT)
		label.pack(pady=10, padx=10, fill='x')

		button_q = ttk.Button(self, text='Quit', width='15', command=lambda: parent.quit())
		button_q.pack()

		button1 = ttk.Button(self, text='Back to Home', width='15', command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button_stop = ttk.Button(self, text='Stop', width='15', command=lambda: controller.show_frame(PageOne))
		button_stop.pack()

		button_start = ttk.Button(self, text='Start', width='15', command=lambda: controller.show_frame(PageOne))
		button_start.pack()

	
		# a.plot([1,2,3,4,5,6,7,8], [5,6,7,1,3,5,6,8])

		canvas = FigureCanvasTkAgg(f, self)
		# # canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# animate()

app = SeaofBTCapp()
# a.canvas.mpl_connect('button_press_event', onClick)
ani = animation.FuncAnimation(f, animate, interval=100)
app.mainloop()




