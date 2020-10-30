
from tkinter import *
import math


root = Tk()
root.title("Постороение графиоков y = sin(x)")
root.geometry("1024x640")

canvas = Canvas(root, width=1020, height=620, bg='#002')

# линии сетки повертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill='#191938') # အောက်ကနေစ မျဉ်းကြောင်းကို စဆွဲ

# линии сетки горизонтали
for x in range(21):
    k = 50 * x
    canvas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#191938') # ပေါ် က နေစ ဆွဲသည်ဆွဲသည်


# линии координат X и Y
canvas.create_line(10, 10, 10, 610, width=1, arrow=FIRST, fill='white') # y axis
canvas.create_line(10, 310, 1010, 310, width=1, arrow=LAST, fill='white') # x axis

# ========================== x(t) = Asin(wt + p) ===============================
w = 0.0309 # циклическая частота
phi = 10 # смещение графика по X
A = 200 #  амплитуда
dy = 310 # смещение графика по Y

xy = []
for x in range(1000):
    y = math.sin(x * w)
    xy.append(x + phi)
    xy.append(y * A + dy)
print(xy)
sin_line = canvas.create_line(xy, fill='blue', width=1)


# l = [0, 0, 100, 100, 10, 310, 0, 300]
# canvas.create_line(l, fill='green')
# print (l)


canvas.pack()
root.mainloop()
