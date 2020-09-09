
import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

	PAD = 10

	MAX_BUTTONS_PRE_ROW = 4

	button_captions = [
		'C', '+/-', '%', '/',
		7, 8, 9, '*',
		4, 5, 6, '-',
		1, 2, 3, '+',
		0, '.', '=', 'sin'

	]

	def __init__(self, controller):
		super().__init__()
		self.controller = controller
		self.title('PyCalc 1.0')

		self.value_var = tk.StringVar()

		self.make_main_frame()
		self.make_entry()
		self.make_buttons()


	def main(self):
		# print ('in main of view')
		self.mainloop()

	def make_main_frame(self):
		self.main_frm = ttk.Frame(self)
		self.main_frm.pack(padx=self.PAD, pady=self.PAD)


	def make_entry(self):
		ent = ttk.Entry(self.main_frm, justify='right', textvariable=self.value_var, \
			state=True)
		ent.pack(fill='x')

	def make_buttons(self):
		outer_frm = ttk.Frame(self.main_frm)
		outer_frm.pack()

		frm = ttk.Frame(outer_frm)
		frm.pack()

		button_in_row = 0

		for caption in self.button_captions:
			if button_in_row == self.MAX_BUTTONS_PRE_ROW:
				frm = ttk.Frame(outer_frm)
				frm.pack()
				button_in_row = 0

			btn = ttk.Button(frm, text=caption)
			btn.pack(side='left')

			button_in_row +=1




















