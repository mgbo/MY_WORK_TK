

from deck import Deck
from hand import Hand
from card import Card
import os
import tkinter as tk

assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Graphical_Blackjack/assets/'))
class GameState:
	def __init__(self):
		self.deck = Deck() # ဖဲ ၅၂ ကတ် ရှိအောင်လုပ်လိုက်တယ်
		self.deck.shuffle() # ထို ဖဲ ၅၂ ကတ်ကို ကုလားဖန်ထိုး လိုက်တယ်

		self.player_hand = Hand() # Player အတွက် လက်တစ်စုံ သတ်မှတ်
		self.dealer_hand = Hand(dealer=True) # ဒိုင်အတွက် လက်တစ်စုံ သတ်မှတ်

		for i in range(2):
			self.player_hand.add_card(self.deck.deal()) # ထိုးသားကို ၅၂ ကတ်ထဲမှ ကတ် ၂ ပေး 
			self.dealer_hand.add_card(self.deck.deal()) # ဒိုင် ကိုလဲ ၂ ကတ်ပေး

		self.has_winner = '' # winder သိရန်အတွက်
			
	def hit(self): # player ဖဲဆွဲရန်အတွက် ၊ ပြီးဘယ်သူ 21 ဖြစ်လား မဖြစ်လား စစ်ရန်အတွက်
		self.player_hand.add_card(self.deck.deal())
		if self.someone_has_blackjack() == 'p':
			self.has_winner = 'p'
		if self.player_is_over():
			self.has_winner = 'd'
	
	# table အခြေအနေ (ဘယ်သူ winner လဲ ၊ player တိုင်ရဲ့ ဖဲအခြေအနေ ပါတဲ့ အချက်အလက်တွေကို dict ဖိုင်အမျိုးအစားနဲ့ ရယူ )
	# need to know (1. p-hand, d-hand, have winner or not, winnner has blackjack or not)
	def get_table_state(self):
		blackjack = False
		winner = self.has_winner

		if not winner:
			winner = self.someone_has_blackjack()
			if winner:
				blackjack = True
		table_state = {
			'player_cards': self.player_hand.cards,
			'dealer_cards': self.dealer_hand.cards,
			'has_winner': winner,
			'blackjack': blackjack,
		}

		return table_state

	def calculate_final_state(self):
		player_hand_value = self.player_hand.get_value()
		dealer_hand_value = self.dealer_hand.get_value()

		if player_hand_value == dealer_hand_value:
			winner = 'dp'
		elif player_hand_value > dealer_hand_value:
			winner = 'p'
		else:
			winner = 'd'

		table_state = {
			'player_cards': self.player_hand.cards,
			'dealer_cards': self.dealer_hand.cards,
			'has_winner': winner,
		}
		return table_state
	
	def someone_has_blackjack(self):
		player = False
		dealer = False

		if self.player_hand.get_value() == 21:
			player = True

		if self.dealer_hand.get_value() == 21:
			dealer = True

		if player and dealer:
			return 'dp'

		elif player:
			return 'p'

		elif dealer:
			return 'd'

		return False

	def player_score_as_text(self):
		return 'Score: ' + str(self.player_hand.get_value())


	def player_is_over(self):
		return self.player_hand.get_value() > 21


class GameScreen(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("BlackJack")
		self.geometry("800x640+0+0")
		self.resizable(False, False)

		self.CARD_ORIGINAL_POSITION = 100 # x coordinate
		self.CARD_WIDTH_OFFSET = 100 # how much space will 
		self.PLAYER_CARD_HEIGHT = 300
		self.DEALER_CARD_HEIGHT = 100
		self.PLAYER_SCORE_TEXT_COORDS = (400, 450)
		self.WINNER_TEXT_COORDS = (400, 250)


		self.game_state = GameState() # ပွဲအစ ဖဲဝေ
		self.game_screen = tk.Canvas(self, bg="gray", width=800, height=500) # GameScreen တည်ဆောက်
		self.bottom_frame = tk.Frame(self, width=800, height=140, bg='red')
		self.bottom_frame.pack_propagate(0)
		

		#===================================== All Buttons =========================================
		self.hit_button = tk.Button(self.bottom_frame, text='Hit', width=25, command=self.hit)
		self.stick_buttton = tk.Button(self.bottom_frame, text='Stick', width=25)
		self.play_again_button = tk.Button(self.bottom_frame, text='Play Again', width=25)
		self.quit_button = tk.Button(self.bottom_frame, text='Quit', width=25, command=self.destroy)
		
		self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
		self.game_screen.pack(side=tk.LEFT, anchor=tk.N)
		self.hit_button.pack(side=tk.LEFT, padx=(100, 200))
		self.stick_buttton.pack(side=tk.LEFT)

		self.display_table() # For drawing the graphical elements into our Canvas

	def hit(self):
		pass

	def display_table(self, hide_dealer=True, table_state=None):
		if not table_state:
			table_state = self.game_state.get_table_state()


		player_card_images = [card.get_file() for card in table_state['player_cards']]
		dealer_card_images = [card.get_file() for card in table_state['dealer_cards']]

		if hide_dealer and not table_state['blackjack']:
			dealer_card_images[0] = Card.get_back_file()


		self.game_screen.delete("all") # clear canvas (game screen)
		self.tabletop_image = tk.PhotoImage(file=assets_folder + "/tabletop.png") # အောက်ခံ image (အစိမ်းရောင်)
		self.game_screen.create_image((400, 250), image=self.tabletop_image) # to put background image
		
		for card_number, card_image in enumerate(player_card_images):
			self.game_screen.create_image(
				(self.CARD_ORIGINAL_POSITION + self.CARD_WIDTH_OFFSET * card_number, self.PLAYER_CARD_HEIGHT), image=card_image)

if __name__ == "__main__":
	app = GameScreen()
	app.mainloop()


























