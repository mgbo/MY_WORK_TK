

class Hand:
	def __init__(self, dealer=False):
		self.dealer = dealer
		self.cards = []
		self.value = 0

	def add_card(self, card):
		self.cards.append(card)

	def calculate_value(self):
		self.value = 0
		has_ace = False
		for card in self.cards:
			if card.value.isnumeric():
				self.value += int(card.value)
			else:
				if card.value == 'A': # A က ဆယ်တစ် 
					has_ace = True
					self.value +=11
				else:
					self.value +=10 # ကျန်တဲ့ J,Q,K က တစ်ဆယ်

			if has_ace and self.value>21:
				self.value -=10

	def get_value(self):
		self.calculate_value()
		return self.value

	def display(self):
		if self.dealer: # အကယ်၍ ဒိုင်ဆိုင် ရင် တစ်ကတ် ဘဲ ပြချင် လို့ list ထဲက value ကို index ဖြင့်ယူလိုက်တယ်
			print ('Hidden')
			print(self.cards[1])

		else:
			for card in self.cards:
				print (card)

			print ("Value :", self.get_value())