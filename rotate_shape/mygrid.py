
import tkinter as tk

LINESIZE = 3
POINTSIZE = 3


class Grid:
	def __init__(self, gwidth=140, gheight=140, scale=5, d=10,\
		minor_color='white', major_color='dark gray', axis_color='black'):
		self.root = tk.Tk()
		self.w = tk.Canvas(self.root, width= gwidth * scale, height= gheight * scale)
		self.w.pack()

		self.x0 = 0
		self.y0 = 0

		self.gwidth = gwidth
		self.gheight = gheight

		self.gltx = -(gwidth//2)
		self.glty = gheight//2

		self.scale = scale # 1 grid unit = scale window pixels
		self.d = d


		self.create()


	def done(self):
		self.root.mainloop()

	# ------ from my coordinate to win coordinate --------------
	def win_coordinate(self, gx, gy):
		x = (gx - self.gltx) * self.scale
		y = (-gy + self.glty) * self.scale

		return x, y

	def draw_line(self, x1, y1, x2, y2, color):
		wx1, wy1 = self.win_coordinate(x1, y1) # from my coordinate to win coordinate
		wx2, wy2 = self.win_coordinate(x2, y2)

		self.w.create_line(wx1, wy1, wx2, wy2, width=LINESIZE, fill=color)


	def line_color(self, n=0):
		if n % 10 != 0:
			return 'white'

	def create(self):
		w = self.w

		#----------------- (x, y) values in my coordinate system ------------
		xmin = self.gltx
		xmax = self.gltx + self.gwidth
		ymin = self.glty - self.gwidth
		ymax = self.glty


		#-------- for vertical line ----------
		i = 0
		for x in range(0, xmax, self.d):
			col = self.line_color(i)
			wx1, wy1 = self.win_coordinate(x, ymin)
			wx2, wy2 = self.win_coordinate(x, ymax)
			w.create_line(wx1, wy1, wx2, wy2, fill=col)
			i += 1

		i = 0
		for x in range(0, xmin, -self.d):
			col = self.line_color(i)
			wx1, wy1 = self.win_coordinate(x, ymin)
			wx2, wy2 = self.win_coordinate(x, ymax)
			w.create_line(wx1, wy1, wx2, wy2, fill=col)
			i += 1

		#------------ for horizontal line --------
		i = 0
		for y in range(0, ymax, self.d):
			col = self.line_color(i)
			wx1, wy1 = self.win_coordinate(xmin, y)
			wx2, wy2 = self.win_coordinate(xmax, y)
			w.create_line(wx1, wy1, wx2, wy2, fill=col)
			i += 1

		i = 0
		for y in range(0, ymin, -self.d):
			col = self.line_color(i)
			wx1, wy1 = self.win_coordinate(xmin, y)
			wx2, wy2 = self.win_coordinate(xmax, y)
			w.create_line(wx1, wy1, wx2, wy2, fill=col)
			i += 1
				#-------- AXIS ------------
		w.create_line(*self.win_coordinate(xmin, 0), *self.win_coordinate(xmax, 0), width=2, fill='black')
		w.create_line(*self.win_coordinate(0, ymin), *self.win_coordinate(0, ymax), width=2, fill='black')



if __name__ == '__main__':
	g = Grid()
	g.done()






