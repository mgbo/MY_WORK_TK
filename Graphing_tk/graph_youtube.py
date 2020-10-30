
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import time
import psutil # cpu အသုံးပြုမှုကိုလိုချင်လို့

# plot data

y = []
x = []
i =0
cond = False

def plot_data():
	global cond, x, y, i
	if cond:
		data = psutil.cpu_percent()
		y.append(data)
		i +=1
		x.append(i)
		print (data, i)

		ax.set_xlim(left=max(0, i-50), right=i+50)
		ax.plot(x,y,'blue')

		canvas.draw()

	root.after(500, plot_data)



def plot_start():
	global cond
	print ('start')
	cond = True

def plot_stop():
	global cond
	print ('stop')
	cond = False


root = tk.Tk()
root.title('Real time plot cpu usage')
root.geometry('800x500')

# =========== for plot ======
fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Serial Data')
ax.set_xlabel('time')
ax.set_ylabel('cup percent')



canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().place(x=100, y=0, width=600, height=400)
canvas.draw()

# ======= create button ======
start = tk.Button(root, text='start', width=15, command=plot_start)
start.place(x=250, y=450)


stop = tk.Button(root, text='stop', width=15, command=plot_stop)
stop.place(x=450, y=450)


root.after(1000, plot_data)
root.mainloop()




















