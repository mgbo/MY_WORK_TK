

import tkinter as tk


def add():
	txt = en.get()
	lbox.insert(tk.END, txt)

def delete():
	''' for one item '''
	# index = lbox.curselection()
	# print (index)
	# lbox.delete(index)

	select = list(lbox.curselection())
	select.reverse()
	for i in select:
		lbox.delete(i)


def save():
	with open('urok_6.txt', 'w') as f:
		f.writelines('\n'.join(lbox.get(0, tk.END)))
		print ('file is save')
		f.close()


root = tk.Tk()

frame_1 = tk.Frame(root)
lbox = tk.Listbox(frame_1, height=15, width=20, selectmode=tk.EXTENDED)
scroll = tk.Scrollbar(command=lbox.yview)
scroll.pack(sid=tk.LEFT, fill=tk.Y)
lbox.config(yscrollcommand=scroll.set)


frame_1.pack(side=tk.LEFT, padx=10)
lbox.pack()


frame_2 = tk.Frame(root)
en = tk.Entry(frame_2, width=20)
btn_1 = tk.Button(frame_2, text='Add', command=add)
btn_2 = tk.Button(frame_2, text='Delete', command=delete)
btn_3 = tk.Button(frame_2, text='Save', command=save)


frame_2.pack(side=tk.LEFT, padx=10)
en.pack(fill=tk.X)
btn_1.pack(fill=tk.X)
btn_2.pack(fill=tk.X)
btn_3.pack(fill=tk.X)


root.mainloop()