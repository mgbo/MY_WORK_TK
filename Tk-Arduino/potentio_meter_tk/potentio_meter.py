
import tkinter as tk
import numpy as np
import threading
import serial


#------ from random ----------------
# def get_data():
# 	threading.Timer(1,get_data).start()
# 	x = np.random.randint(0, 45, 1) # it is list datatype
# 	print (x)
# 	l_d_data.config(text=x[0])
# 	return x[0]

global ser
ser = serial.Serial('/dev/cu.usbmodem14101', timeout=10)

# def check_serial_event():
# 	serial_thread = threading.Timer(1, check_serial_event)
# 	if ser.is_open == True:
# 		serial_thread.start()
# 		if ser.in_waiting:
# 			eol = b'\n'
# 			len_eol = len(eol)
# 			line = bytearray()
# 			print (f"len_eol = {len_eol}, line = {line}")

# 			while True:
# 				c = ser.read(1)
# 				if c:
# 					line += c
# 					print (f"line = {line}")

# 					if line[-len_eol:] == eol:
# 						print (f"line[-len_eol] = {line[-len_eol]} --> {eol}")
# 						break
# 				else:
# 					break

# 			print (f"line after while = {line}")
# 			line = line.rstrip()
# 			print (f"line = {line}")
# 			ser_data = line.decode("utf-8")
# 			print (f"ser_data = {ser_data}")
# 			l_d_data.config(text=ser_data)



# =========== mehod -2 =============
# def check_serial_event_2():

# 	serial_thread = threading.Timer(1, check_serial_event_2)
# 	if ser.is_open == True:
# 		serial_thread.start()
# 		if ser.in_waiting:
# 			c = ser.readline()
# 			print (f"c : {c}")

# 			line = c.decode("utf-8").rstrip()
# 			print (f"line : {line}")



def check_serial_event_3():
	if ser.is_open == True:
		if ser.in_waiting:
			c = ser.readline()
			print (f"c : {c}")

			line = c.decode("utf-8").rstrip()
			print (f"line : {line}")
			l_d_data.config(text=line)
		l_d_data.after(100, check_serial_event_3)


mainwindow = tk.Tk()
mainwindow.geometry('640x340')
mainwindow.title('Sensor data')


l_d = tk.Label(mainwindow, text='Sensor data', font=("Arial", 22), fg='red')
# l_d.pack()
l_d.grid(row=0, column=0, padx=10, pady=10)

l_d_data = tk.Label(mainwindow, font=("Arial", 22))
l_d_data.grid(row=0, column=2, padx=10, pady=10)

# get_data()
check_serial_event_3()

mainwindow.mainloop()


