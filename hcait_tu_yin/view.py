

import tkinter as tk
from configurations import *
from controller import Controller


class View:
	board_color_1 = BOARD_COLOR_1
	board_color_2= BOARD_COLOR_2

	def __init__(self, parent, controller):
		self.controller = controller
		self.parent = parent
		self.create_chess_base()
		self.canvas.bind("<Button-1>", self.on_square_clicked) # chess board မှာ အကွက်များ၏ row, column သိရှိနိုင်ရန်အတွက်

	def create_chess_base(self):
		self.create_top_menu() # အပေါ်က menu bar အတွက်
		self.create_canvas() # chess ခုံ တည်ဆောက်ရန် အတွက် canvas ဆွဲ
		self.draw_board() # canvas ပေါ်တွင် chess ခုံ ရေးဆွဲ
		self.create_bottom_frame() # 

	#=================== chess ခုံ တည်ဆောက်ရန် အတွက် ၅၁၂ ၅၁၂ pixel ရှိသော canvas  တည်ဆောက် ============
	def create_canvas(self):
		canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE # 8 x 64 = 512
		canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE # 8 x 64 = 512
		self.canvas = tk.Canvas(self.parent, width=canvas_width, height=canvas_height)
		self.canvas.pack(padx=8, pady=8)

	#============================= draw board ==================================
	def draw_board(self):
		current_color = BOARD_COLOR_2
		for row in range(NUMBER_OF_ROWS):
			current_color = self.get_alternate_color(current_color)
			for col in range(NUMBER_OF_COLUMNS):
				x1, y1 = self.get_x_y_coordinate(row, col)
				x2, y2 = x1 + DIMENSION_OF_EACH_SQUARE, y1 + DIMENSION_OF_EACH_SQUARE
				self.canvas.create_rectangle(x1, y1, x2, y2, fill=current_color)
				current_color = self.get_alternate_color(current_color)

	def get_x_y_coordinate(self, row, col):
		x = (col * DIMENSION_OF_EACH_SQUARE)
		y = ((7 - row) * DIMENSION_OF_EACH_SQUARE)
		return (x,y)

	def get_alternate_color(self, current_color):
		if current_color == self.board_color_2:
			next_color = self.board_color_1
		else:
			next_color = self.board_color_2

		return next_color

	# ================= to know cell position (x,y) using mouse click ===============
	def on_square_clicked(self, event):
		clicked_row, clicked_column = self.get_clicked_row_column(event)
		print ('Hey you clicked on', clicked_row, clicked_column)

	def get_clicked_row_column(self, event):
		col_size = row_size = DIMENSION_OF_EACH_SQUARE
		print (f"x:{event.x}, y:{event.y}") # mouse position (x,y) ကို သိချင်လို့
		clicked_column = event.x // col_size
		clicked_row = 7 - (event.y // row_size) # အောက်ကနေစတဲ့ အကွက် နံပါတ် လိုချင်လို့ စုစုပေါင်းကွက်အရေအတွက် ထဲက နုတ်လိုက်တာ

		return (clicked_row, clicked_column)

	#================ Create Menu bar ===========================
	def create_top_menu(self):
		self.menu_bar = tk.Menu(self.parent) # this is main menu bar
		self.create_file_menu()
		self.create_edit_menu()


	def create_file_menu(self):
		self.file_menu = tk.Menu(self.menu_bar, tearoff=0) 
		self.file_menu.add_command(
			label="New Game", command=self.on_new_game_menu_clicked) #  menu ဘားပေါ်မှာ menu name (New Game) အမည်နှင့်ထည့်

		self.menu_bar.add_cascade(label="File", menu=self.file_menu)
		self.parent.config(menu=self.menu_bar)

	def on_new_game_menu_clicked(self):
		pass

	def create_edit_menu(self):
		self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)

		self.edit_menu.add_command(
			label="Preference", command=self.on_preference_menu_clicked)
		self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
		self.parent.config(menu=self.menu_bar)

	def on_preference_menu_clicked(self):
		pass

	# =================== ကစားသူများအား အသိပေးကြော်ငြော် ရန် အတွက် စာရေးရန် နေရာ ===================
	def create_bottom_frame(self):
		self.bottom_frame = tk.Frame(self.parent, height=64)
		self.info_label = tk.Label(self.bottom_frame, text='  White to start the Game  ', fg=BOARD_COLOR_2)

		self.info_label.pack(side=tk.RIGHT, padx=8, pady=8)
		self.bottom_frame.pack(fill="x", side="bottom")



def main(controller):
	root = tk.Tk()
	root.title('chess')
	View(root, controller)
	root.mainloop()

def init_new_game():
	game_controller = Controller
	main(game_controller)


if __name__ == '__main__':
	init_new_game()












