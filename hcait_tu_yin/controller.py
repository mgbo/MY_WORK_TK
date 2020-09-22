
'''
controller သည် model နှင့်ချိတ်ဆက် ထားပြီး ၎င်း ၏ အချက်အလက်များကို ရယူထားသည်
ကျွန်တော် အခြေအနေတွင် model သည် dictionary data type အမျိုးအစားဖြစ်သည်

'''

from configurations import *
import model
import piece

class Controller:
	def __init__(self):
		self.init_model()

	def init_model(self):
		self.model = model.Model()
		print ("Init model in controller")
		for k,v in self.model.items():
			print (k,v)
	
	# ဉပမာ A1 --> 0, 7
	def get_numeric_notation(self, position): # model dictionary မှာ key(position) ဖြင့် row, column နံပါတ်ရယူရန် အတွက်
		return piece.get_numeric_notation(position)
	
	def get_all_pieces_on_chess_board(self):
		print ("Get all pieces on chess board")
		for k, v in self.model.items():
			print (k,v)
		return self.model.items()
	
	def reset_game_data(self):
		self.model.reset_game_data()
	
	def reset_to_initial_locations(self):
		self.model.reset_to_initial_locations()
























