
import cv2
from PIL import Image
from PIL import ImageTk
import tkinter


class VideoString:
	def __init__(self):
		self.root = tkinter.Tk()
		self.root.title('video')
		self.root.geometry("600x600")

		self.metka = tkinter.Label(self.root)
		self.metka.pack()

		self.metka_2 = tkinter.Label(self.root, text='hello', width=200)
		self.metka_2.pack()


		#----- инициализировать камера -----
		self.kamera = cv2.VideoCapture(0)

		self.camera()

	def camera(self):
		ret, frame = self.kamera.read()
		# sveta = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		sveta = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		frame = Image.fromarray(frame)
		frame = ImageTk.PhotoImage(frame)
		self.metka.configure(image=frame)
		self.metka.image = frame
		self.metka.after(1, self.camera)

	def done(self):
		self.root.mainloop()


if __name__ == '__main__':

	objVideo = VideoString()
	objVideo.done()
