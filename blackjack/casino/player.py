
from .hand import Hand

class Player:
	def __init__(self):
		self.money = 50
		self.hand = Hand()
	
	def add_winnings(self, winnings): 
		self.money += winnings
	
	def can_place_bet(self, amount): # လောင်းကြေးတည့်ရန်အတွက် ပိုက်ဆံလောက်လား မလောက်ဘူးလား စစ်ဆေးရန်အတွက်
		return self.money>=amount
	
	def place_bet(self, amount): # လောင်းကြေးထည့် ရန်အတွက်
		self.money -=amount
	
	def receive_card(self, card):
		self.hand.add_card(card)
	
	def empty_hand(self):
		self.hand.cards = []
	
	@property
	def score(self):
		# print ("Hand get score : ", self.hand.get_value())
		return self.hand.get_value()

	@property
	def is_over(self):
		return self.hand.get_value() > 21

	@property
	def has_blackjack(self):
		return self.hand.get_value() == 21

	@property
	def cards(self):
		return self.hand.cards

class Dealer(Player):
	pass



