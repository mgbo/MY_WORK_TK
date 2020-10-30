
import psutil # cpu အသုံးပြုမှုကိုလိုချင်လို့
import numpy
import matplotlib.pyplot as plt
from drawnow import *
import sys
from matplotlib.figure import Figure


temf = []
x = []
count = 0
# plt.ion()

f = Figure()
a = f.add_subplot(111)
def makeFig():
	# plt.grid(True)
	plt.plot(temf, 'ro-')
	# a.plot(x,temf, 'r0-')
	# plt.twinx()

def draw_plot():
	global count

	while True:
		data = psutil.cpu_percent()
		temf.append(data)
		# x.append(count)
		drawnow(makeFig)
		plt.pause(.0001)
		count +=1
		if count>50:
			temf.pop(0)
			# pass


if __name__ == '__main__':
	try:
		draw_plot()

	except KeyboardInterrupt:
		print ('\nClose Pls')
		sys.exit()







