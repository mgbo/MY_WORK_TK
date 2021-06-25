
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.v_l = QVBoxLayout()
		self.feed_label = QLabel()
		self.v_l.addWidget(self.feed_label)


		self.cancel_btn = QPushButton('Cancel')
		self.cancel_btn.clicked.connect(self.cancelFeed)
		self.v_l.addWidget(self.cancel_btn)

		self.worker1 = Worker()
		self.worker1.start()
		self.worker1.img_update.connect(self.imgUpdateSlot)

		self.setLayout(self.v_l)

	def imgUpdateSlot(self, image):
		self.feed_label.setPixmap(QPixmap.fromImage(image))

	def cancelFeed(self):
		self.worker1.stop()


class Worker(QThread):
	img_update = pyqtSignal(QImage)

	def run(self):
		self.ThreadActive = True
		capture = cv2.VideoCapture(0)

		while self.ThreadActive:
			b, frame = capture.read()

			if b:
				image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				flipped_img = cv2.flip(image, 1)
				convert_q_format = QImage(flipped_img.data, flipped_img.shape[1],\
					flipped_img.shape[0], QImage.Format_RGB888)
				pic = convert_q_format.scaled(640, 480, Qt.KeepAspectRatio)

				self.img_update.emit(pic)

	def stop(self):
		self.ThreadActive = False
		self.quit()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	root = MainWindow()
	root.show()
	sys.exit(app.exec_())





