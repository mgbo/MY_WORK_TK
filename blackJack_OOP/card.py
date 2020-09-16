import random

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return " of ".join((self.value, self.suit))

class Deck:
	def __init__(self):
		self.cards = [Card(s, v) for s in ["Spade", 'Heart','Diamond', 'Club']
									for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

	def shuffle(self):
		if len(self.cards) > 1:
			random.shuffle(self.cards)

	def deal(self):
		if len(self.cards) > 1:
			return self.cards.pop(0)


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

class Game:
	def __init__(self):
		playing = True

		while playing:
			self.deck = Deck() # ဖဲ ၅၂ ကတ် ရှိအောင်လုပ်လိုက်တယ်
			self.deck.shuffle() # ထို ၅၂ ကတ်ကို မွှေ လိုက်တယ်

			self.player_hand = Hand()
			self.dealer_hand = Hand(dealer=True)

			for i in range(2):
				self.player_hand.add_card(self.deck.deal()) # ထိုးသားကို ၅၂ ကတ်ထဲမှ ကတ် ၂ ပေး 
				self.dealer_hand.add_card(self.deck.deal()) # ဒိုင် ကိုလဲ ၂ ကတ်ပေး

			print("Player's hand is :")
			self.player_hand.display()

			print()
			print("Dealer's hand is :")
			self.dealer_hand.display()

			game_over = False

			while not game_over:
				# ဒိုင်ရော ထိုးသားရော 21 ဖြစ်လားမဖြစ်ဘူးလား ဖဲဝေဝေ ပြီးချင် စစ်
				player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack() 

				# နှစ်ယောက်ထဲက တစ်ယောက်ယောက်က 21 ဖြစ်ရင် ဂိမ်းပြီးဆုံး ၂၁ ဖြစ်တဲ့သူ နိုင်
				if player_has_blackjack or dealer_has_blackjack:
					game_over = True
					self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
					continue

				choice = input("Choice h or s --> ").lower() # ထပ်ဆွဲမလား မဆွဲဘူးလား ရွှေးချယ်ရန်အတွက်

				# ကတ်ထပ်ဆွဲမည်ဆိုသော စကားလုံး ဒါမှမဟုတ် မဆွဲမည်ဆိုသော စကားလုံးကို မရွှေးချယ်ခဲ့လျှင် ထပ် ရွှေးချယ်နိုင်ရန် အတွက်
				while choice not in ['h', 's']:
					choice = input("Choice h or s -->").lower()
				

				if choice in ['h']:
					self.player_hand.add_card(self.deck.deal())
					self.player_hand.display()
					
					if self.player_is_over(): # 21 ကျော်သွားရင် ရှုံးပြီ
						print ("You lost\n")
						game_over = True

				else:
					player_hand_value = self.player_hand.get_value()
					dealer_hand_value = self.dealer_hand.get_value()

					print ('\nFinal Results')
					print ('Your hand:', self.player_hand.get_value())
					print("Dealer's hand:", self.dealer_hand.get_value())

					if player_hand_value > dealer_hand_value:
						print ("You Win")
					
					elif player_hand_value == dealer_hand_value:
						print ('Tie')
					
					else:
						print ('Dealer Wins')
					
					game_over = True
		
			again = input("You want to play again? [Y/N] ")

			while again.lower() not in ['y', 'n']:
				again = input("Please enter Y or N")

			if again.lower() == 'n':
				playing = False
			else:
				game_over = False
				
	def check_for_blackjack(self):
		player = False
		dealer = False

		if self.player_hand.get_value() == 21:
			player = True

		if self.dealer_hand.get_value() == 21:
			player = True

		return player, dealer

	def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
		if player_has_blackjack and dealer_has_blackjack:
			print ("Both player have blackjack, Draw!!")
		
		elif player_has_blackjack:
			print ('You Win')
		
		elif dealer_has_blackjack:
			print ('Dealer Win')
		
	def player_is_over(self):
		return self.player_hand.get_value() > 21
	
if __name__ == "__main__":
	game = Game()






















