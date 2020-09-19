

import os
import tkinter as tk

assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'assets/'))
print (assets_folder) # /Users/myomaung/My_data/MY_WORK_TK/assets

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		self.img = tk.PhotoImage(file=assets_folder + '/' + 'resized_' + self.value + '_of_' + self.suit + ".png")
		

	def __repr__(self):
		return " of ".join((self.value, self.suit))

	def get_file(self):
		# print (self.value, self.suit)
		return self.img
	
	@classmethod
	def get_back_file(cls):
		# cls.back = tk.PhotoImage(file=assets_folder + "/resized_hidden_2.png")
		cls.back = tk.PhotoImage(file=assets_folder + "/card-b.png")
		return cls.back
	



















