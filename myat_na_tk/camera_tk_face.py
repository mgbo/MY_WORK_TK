

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import time

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl

import os

face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
print(face_cascade)
class App:
	def __init__(self, video_source=0):
		self.appName = "Camera v1.0"
		self.window = tk.Tk()
		self.window.title(self.appName)
		self.window.resizable(0, 0)
		# self.window.wm_iconbitmap("filename.ico")

		self.window['bg'] = 'black'
		self.video_source = video_source

		self.vid = MyCamera(self.video_source)
		# self.label = tk.Label(self.window, text=self.appName, font=15, \
		# 	bg='blue', fg='white').pack(side=tk.TOP, fill=tk.BOTH)

		# create a canvas that can fit the above video soure side
		self.canvas = tk.Canvas(self.window, width=self.vid.width, height=self.vid.height, bg='red')
		self.canvas.pack()


		self.btn_snapshot = tk.Button(self.window, text='Snapshot', width=30, bg='goldenrod2',\
			activebackground='red', command=self.snapshot)
		self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)


		self.update()
		self.window.mainloop()

	def snapshot(self):
		check, frame = self.vid.getFrame()

		if check:
			img_name = "IMG-" + time.strftime("%H-%M-%S-%d-%m") + ".jpg"
			cv2.imwrite(img_name, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

			# msg = tk.Label(self.window, text='image saved ' + image, bg='black', fg='green').place(x=430, y=510)

			#============ play sound to ensure photo is taken ================
			# file = QUrl("Camera shutter.wav")
			# content = QMediaContent(file)
			# self.player = QMediaPlayer()
			# self.player.setMedia(content)
			# self.player.play()

	def update(self):
		b, frame = self.vid.getFrame()

		if b:
			self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
			self.canvas.create_image(0, 0, image = self.photo, anchor= tk.NW)

		self.window.after(15, self.update)

class MyCamera:
	def __init__(self, video_source=0):

		self.vid = cv2.VideoCapture(video_source)


		if not self.vid.isOpened():
			raise ValueError("Unable to open This camera", video_source)

		# self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		# self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

		#---- resize camera frame-----------
		self.width = 640
		self.height = 480
		self.vid.set(3, 640)
		self.vid.set(4, 480)

	def getFrame(self):
		if self.vid.isOpened():
			b, frame = self.vid.read()

			if b:
				# return (b, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)) #BGR2RGB, BGR2GRAY
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(120, 120))
				for (x, y, w, h) in faces:
					cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)

				return b, gray

			else:
				return (b, None)
		else:
			return (b, None)

	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()


if __name__ == '__main__':
	myapp = App()






















