
import tkinter as tk
from functools import partial
from casino import Card, Deck, Player, Dealer, assets_folder
from casino_sounds import SoundBoard

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack")
        self.geometry("800x640")
        self.resizable(False, False)

        #============== BUTTON Frame ================
        self.bottom_frame = tk.Frame(self, width=800, height=140, bg="red")
        self.bottom_frame.pack_propagate(0)


        #====================== All Button ============================
        self.hit_button = tk.Button(self.bottom_frame, text="Hit", width=25)
        self.stick_button = tk.Button(self.bottom_frame, text="Stick", width=25)
        self.next_round_button = tk.Button(self.bottom_frame, text="Next Round", width=25)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", width=25, command=self.destroy)
        self.new_game_button = tk.Button(self.bottom_frame, text="New Game", width=25)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # self.game_screen = GameScreen(self, bg="white", width=800, height=500)
        # self.game_screen.pack(side=tk.LEFT, anchor=tk.N)


        # self.game_screen.setup_opening_animation()


if __name__ == "__main__":
	pass

















