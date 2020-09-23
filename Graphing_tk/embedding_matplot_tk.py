
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style


import tkinter as tk
from  tkinter import ttk

import os

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animate(i):
	# with open("sampleData.txt", 'r') as f:

	pullData = open("sampleData.txt", "r").read()
	dataList = pullData.split('\n')
	print(dataList)
	# print (f"({dataList[0]}, {dataList[1]})")
	xList = []
	yList = []

	for eachLine in dataList:
		print (eachLine)
		if len(eachLine) > 1:
			x, y = eachLine.split(',')
			xList.append(int(x))
			yList.append(int(y))

	a.clear()
	a.plot(xList, yList)


loc_img = os.path.abspath(os.path.join(os.path.dirname(__file__),'hla.ico'))
print (loc_img)



class SeaofBTCapp(tk.Tk):
	def __init__(self, *arg, **kwargs):
		tk.Tk.__init__(self, *arg, **kwargs)
		# tk.Tk.iconbitmap(self, default='ship.ico')
		# tk.Tk.wm_title(self, "sea of BTC client")

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
			frame = F(containter, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
			self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise() # လေ့လာရန်


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Start Page', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button = ttk.Button(self, text='Visti Page 1', command=lambda: controller.show_frame(PageOne))
		button.pack()


		button2 = ttk.Button(self, text='Visti Page 2', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text='Graph Page', command=lambda: controller.show_frame(PageThree))
		button3.pack()	



class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Page One!!', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text='Back to Page Two', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Page Two!!', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text='Back to PageOne', command=lambda: controller.show_frame(PageOne))
		button2.pack()

		button3 = ttk.Button(self, text='Back to Graph Page', command=lambda: controller.show_frame(PageThree))
		button3.pack()

class PageThree(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Graph Page!!', font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
		button1.pack()

		# button2 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(PageOne))
		# button2.pack()

	
		# a.plot([1,2,3,4,5,6,7,8], [5,6,7,1,3,5,6,8])

		canvas = FigureCanvasTkAgg(f, self)
		# # canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# toolbar = NavigationToolbar2TkAgg(canvas, self)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# animate()

app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()




