
import tkinter as tk

root = tk.Tk()

lbox = tk.Listbox(root, width=15, height=8)
lbox.pack()


for i in ('one', 'two', 'tree', 'four'):
	lbox.insert(0, i)

root.mainloop()