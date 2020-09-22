
from configurations import *
import piece


class Model(dict):
	captured_pieces = {'white':[], 'black':[]}
	player_turn = None
	halfmove_clock = 0
	fullmove_number = 1
	history = []
	
	def __init__(self):
		self.reset_to_initial_locations()
	
	def get_piece_at(self, position): # ခုလက်ရှိအခြေအနေမှာ key (position) ဖြင့် value ကိုရယူခြင်းဖြစ်ပါသည်
		return self.get(position)
	
	def get_alphanumberic_position(self, rowcol):  # row, column များကို သတ်မှတ်ထားသောပုံစံသို့ ပြောင်းလဲ 0,0 --> A1
		if self.is_on_board(rowcol): 
			row, col = rowcol
			return "{}{}".format(X_AXIS_LABELS[col], Y_AXIS_LABELS[row])
	
	def is_on_board(self, rowcol): # စစ်တုရင် ခုံ အတွင်း ရှိမရှိ စစ်ဆေးရန် အတွက်
		row, col = rowcol
		return 0<= row <=7 and 0<=col <=7
	
	def reset_game_data(self): # model ရှိ data များကို အစက ပြန် စလိုက်ခြင်း ဖြစ်သည်
		captured_pieces = {'white':[], 'black': []}
		player_turn = None
		halfmove_clock = 0
		fullmove_number = 1
		history = []
	
	def reset_to_initial_locations(self):
		self.clear() # လက်ရှိ dict ကို အလွတ်ထားလိုက်တယ်
		# if not self:
		# 	print ('это пустой словарь')
		# else:
		# 	print ('не пустой словарь')
		# 	for k, v in self.items():
		# 		print ('Началое состояние :', k, v)

		for position, value in START_PIECES_POSITION.items():# {"A8": "r",}
			self[position] = piece.create_piece(value) # သူရဲ့ position ပေါ်မှုတည်ပြီ သက်ဆိုင်ရာ စစ်တုရင် အရုပ် တည်ဆောက်
			self[position].keep_reference(self)
		self.player_turn = 'white'














