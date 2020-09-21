
from configurations import *


def create_piece(piece, color='white'):
	if isinstance(piece, str):
		if piece.upper() in SHORT_NAME.keys():
			if piece.isupper():
				color = "white"
			else:
				color = "black"
		piece = SHORT_NAME[piece.upper()] # SHORT_NAME dictionary ကို key ဖြင့် value ရရှိရန် 
		print ('piece : ', piece)
		if piece in SHORT_NAME.values():
			return eval("{classname} (color)".format(classname=piece))

	raise exceptions.ChessError("invalid piece name : '{}'".format(piece))




class Piece:
	def __init__(self, color):
		# __name__ is a built-in variable which evaluates to the name of the current module
		self.name = self.__class__.__name__.lower() # filename ပြန်ရမည် (piece)
		if color == 'black':
			self.name = self.name.lower()# 

		elif color == 'white':
			self.name = self.name.upper()
		
		self.color = color

	def keep_reference(self, model):
		self.model = model

class King(Piece):
	pass

class Queen(Piece):
	pass

class Rook(Piece):
	pass

class Bishop(Piece):
	pass

class Knight(Piece):
	pass

class Pawn(Piece):
	pass




