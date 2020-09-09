
from model import Model
from view import View



class Controller:

	def __init__(self):
		self.model = Model()
		self.view = View(self)


	def main(self):
		# print ('In main of controller')
		self.view.main()

	def on_button_click(self, caption):
		print (f'Button {caption} click')




if __name__ == "__main__":
	# print ("Hello World!!")

	calculator = Controller()
	calculator.main()


