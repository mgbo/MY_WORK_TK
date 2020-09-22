

import tkinter as tk
from configurations import *
import controller
import os


assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pieces_image/'))
print (assets_folder) # ပုံများကို သိမ်း ထားသော ဖိုင်တည်နေရာ path ကိုရရှိရန်

class View:
	images = {} # စစ်တုရင် နယ်အရုပ်များ သိမ်းဆည်းထားရန်အတွက်
	board_color_1 = BOARD_COLOR_1
	board_color_2= BOARD_COLOR_2

	def __init__(self, parent, controller):
		self.controller = controller
		self.parent = parent
		self.create_chess_base() # အရုပ်များမပါသော စစ်တုရင် ခုံ ၊ လိုအပ်သောစာတမ်း ၊ menubar များကိုထည့်သွင်း
		self.canvas.bind("<Button-1>", self.on_square_clicked) # chess board မှာ အကွက်များ၏ row, column သိရှိနိုင်ရန်အတွက်
		self.start_new_game() # စစ်တုရင်ခုံ ပေါ်တွင် သက်ဆိုင်ရာ နယ်ရုပ်များကို သတ်မှတ်ထားသော နေရာများတွင် နေရာ ချ ရန်အတွက်


	def create_chess_base(self):
		self.create_top_menu() # အပေါ်က menu bar အတွက်
		self.create_canvas() # chess ခုံ တည်ဆောက်ရန် အတွက် canvas ဆွဲ
		self.draw_board() # canvas ပေါ်တွင် chess ခုံ ရေးဆွဲ
		self.create_bottom_frame() # 

	#=================== chess ခုံ တည်ဆောက်ရန် အတွက် ၅၁၂ ၅၁၂ pixel ရှိသော canvas  တည်ဆောက် ============
	def create_canvas(self):
		canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE # 8 x 64 = 512
		canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE # 8 x 64 = 512
		self.canvas = tk.Canvas(self.parent, width=canvas_width, height=canvas_height) # canvas class ကို root window နှင့် ချိတ်ဆက်ရန်အတွက်
		self.canvas.pack(padx=8, pady=8) # canvas ကို နေရာချရန်အတွက်

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

	#=================== စစ်တုရင်မှ အရုပ်များ ကို ရေးဆွဲရန် posisition(x,y) နှင့် သတ်ဆိုင်ရာ အရုပ်သတ်မှတ်ခြင်း နှင့် model data နှင့် ချိတ်ဆက်ခြင်း =======================

	def start_new_game(self):
		self.controller.reset_game_data()
		self.controller.reset_to_initial_locations()
		self.draw_all_pieces()

	def draw_single_piece(self, position, piece):
		x, y = self.controller.get_numeric_notation(position) # x, y ကို ကိန်းဂဏန်း ဖြင့် ရရှိရန်အတွက်

		if piece:
			filename = f"{assets_folder}/{piece.name.lower()}_{piece.color}.png"
			if filename not in self.images: # filename ဖြင့် images(dict) ထဲတွင် သိမ်းဆည်းရန်အတွက်
				self.images[filename] = tk.PhotoImage(file=filename)

			# for k, v in self.images.items():
			# 	print ('images files -->', k,v)

			x0, y0 = self.calculate_piece_coordinate(x, y) # နယ်ရုပ် ထားရမည့် တည်နေရာရရှိရန် အတွက်
			self.canvas.create_image(x0, y0, image=self.images[
									 filename], tags=("occupied"), anchor="c")
	
	def calculate_piece_coordinate(self, row, col):
		x0 = (col * DIMENSION_OF_EACH_SQUARE) + int(DIMENSION_OF_EACH_SQUARE/2)
		y0 = ((7-row) * DIMENSION_OF_EACH_SQUARE) + int (DIMENSION_OF_EACH_SQUARE/2)
		return (x0, y0)
	
	def draw_all_pieces(self):
		self.canvas.delete("occupied")
		for position, piece in self.controller.get_all_pieces_on_chess_board():
			self.draw_single_piece(position, piece)

def main(controller):
    root = tk.Tk()
    root.title("Chess")
    View(root, controller)
    root.mainloop()


def init_new_game():
    game_controller = controller.Controller()
    main(game_controller)

if __name__ == "__main__":
    init_new_game()








