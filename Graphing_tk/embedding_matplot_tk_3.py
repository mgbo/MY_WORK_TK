
# import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import psutil # cpu အသုံးပြုမှုကိုလိုချင်လို့

import tkinter as tk
from  tkinter import ttk
LARGE_FONT = ("Verdana", 12)

y = []
x = []
i =0
cond = False

f = Figure()
a = f.add_subplot(111)

class SeaofBTCapp(tk.Tk):
	def __init__(self, *arg, **kwargs):
		tk.Tk.__init__(self, *arg, **kwargs)
		self.geometry("800x640")
		self.resizable(False, False)

		containter = tk.Frame(self) # tk.Tk root ထဲမှာ frame ထည့်
		containter.pack(side='top', fill='both', expand=True)
		containter.grid_rowconfigure(0, weight=1)# To change this for a given widget
		containter.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageGraph):
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
	def __init__(self, parent, controller): # parent - (for containter (frame)) , controller - for (main tk.Tk root အတွက်)
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Start Page', bg='#ffb3fe', fg='green', font=LARGE_FONT)
		label.pack(pady=10, padx=10, fill='x')

		button_q = ttk.Button(self, text='Quit', width='20', command=lambda: controller.quit())
		button_q.place(x=300, y=50)


		button3 = ttk.Button(self, text='Graph Page', width='20', command=lambda: controller.show_frame(PageGraph))
		button3.place(x=450, y=50)

		label_1 = tk.Label(self, text='ပထမ စာမျက်နှာမှကြိုဆိုပါတယ်', fg='green', font=LARGE_FONT)
		label_1.place(x=300, y=320)


class PageGraph(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		label = tk.Label(self, text='Graph Page!!', bg='blue', font=LARGE_FONT)
		label.pack(pady=10, padx=10, fill='x')

		button_q = ttk.Button(self, text='Quit', width='20', command=lambda: controller.quit())
		button_q.place(x=100, y=50)

		button1 = ttk.Button(self, text='Back to Home', width='20', command=lambda: controller.show_frame(StartPage))
		button1.place(x=250, y=50)
		
		button_stop = ttk.Button(self, text='Stop', width='20', command= self.plot_stop)
		button_stop.place(x=400, y=50)

		button_start = ttk.Button(self, text='Start', width='20', command= self.plot_start)
		button_start.place(x=550, y=50)


		self.canvas = FigureCanvasTkAgg(f, self)
		# self.canvas.get_tk_widget().pack(side='bottom', fill=tk.BOTH)
		self.canvas.get_tk_widget().place(x=100, y=100)

		self.plot_data()

	def plot_data(self):
		global cond, x, y, i
		if cond:
			data = psutil.cpu_percent()
			y.append(data)
			i +=1
			x.append(i)
			print (data, i)

			# a.set_xlabel('time')
			# a.set_ylabel('cup usage percentage')
			a.set_xlim(left=max(0, i-50), right=i+50)
			a.plot(x,y,'b-')

			self.canvas.draw()
		self.after(1000, self.plot_data)

	def plot_start(self):
		global cond
		print ('start')
		cond = True

	def plot_stop(self):
		global cond
		print ('stop')
		cond = False

app = SeaofBTCapp()
app.mainloop()












