

import tkinter as tk
from contact import Contact
from tkinter import messagebox as mb

class ContactList(tk.Frame):
	def __init__(self, master, **kwargs):
		super().__init__(master)
		self.lb = tk.Listbox(self, **kwargs)
		scroll = tk.Scrollbar(self, command=self.lb.yview)
		self.lb.config(yscrollcommand=scroll.set)

		self.lb.pack(side=tk.LEFT, fill=tk.Y)
		scroll.pack(side=tk.RIGHT, fill=tk.BOTH, expand = 1)

	def insert(self, contact, index=tk.END):
		text ="{} {}".format(contact.last_name, contact.first_name)
		self.lb.insert(index, text)

	def delete(self, index):
		self.lb.delete(index, index)

	def update(self, contact, index):
		self.delete(index)
		self.insert(contact, index)

	def bind_doble_click(self, callback):
		handler = lambda _: callback(self.lb.curselection()[0])
		self.lb.bind("<Double-Button-1>", handler)


class ContactForm(tk.LabelFrame):
	field = ('Last Name', 'First Name', 'Email', 'Phone')

	def __init__(self, master, **kwargs):
		super().__init__(master, text='Contact', padx=10, pady=10, **kwargs)
		self.frame = tk.Frame(self)
		self.frame.pack(expand=1)

		self.labels = [tk.Label(self.frame, text=name) for name in self.field]
		self.entries = [tk.Entry(self.frame) for _ in self.field]
		self.widgets = list(zip(self.labels, self.entries))

		for i, (label, entry) in enumerate(self.widgets):
			label.grid(row=i, column=0, sticky=tk.W)
			entry.grid(row=i, column=1)

	# 	self.entries = list(map(self.create_field, enumerate(self.field)))

	# def create_field(self, field):
	# 	position, text = field
	# 	label = tk.Label(self.frame, text=text)
	# 	entry = tk.Entry(self.frame, width=25)
	# 	label.grid(row=position, column=0, pady=5)
	# 	entry.grid(row=position, column=1, pady=5)
	# 	return entry

	# Contact Form တွင်ထည့်ရန်
	def load_detail(self, contact): 
		values = (contact.last_name, contact.first_name, contact.email, contact.phone)

		for entry, value in zip(self.entries, values):
			entry.delete(0, tk.END)
			entry.insert(0, value)

	# Contact Form မှာ အသုံးပြုသူ ရေးတဲ့ အချက်အလက်များကို Contact object အဖြစ်ရယူ
	def get_details(self):
		values = [e.get() for e in self.entries]
		try:
			# print (Contact(*values))
			return Contact(*values)
		except ValueError as e:
			mb.showerror("Validation Error", str(e), parent=self)

	def clear(self):
		for entry in self.entries:
			entry.delete(0, tk.END)


class NewContact(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.contact = None
		self.form = ContactForm(self)
		self.btn_add = tk.Button(self, text='Confirm', command=self.confirm)

		self.form.pack(padx=10, pady=10)
		self.btn_add.pack(pady=10)
	
	def confirm(self):
		# get detail က  Contact Form ကနေ အသုံးပြုသူ ရေးတဲ့ အချက်အလက်များကို Contact object အဖြစ်ရယူ
		self.contact = self.form.get_details()
		if self.contact:
			self.destroy()

	def show(self):
		self.grab_set()
		self.wait_window()
		return self.contact


class UpdateContactForm(ContactForm):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)
		self.btn_save = tk.Button(self, text='save')
		self.btn_delete = tk.Button(self, text='delete')

		self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
		self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
	
	def bind_save(self, callback):
		self.btn_save.config(command=callback)
	
	def bind_delete(self, callback):
		self.btn_delete.config(command=callback)


class ContactView(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("SQLite Contacts List")

		self.list = ContactList(self, height=15)
		self.form = UpdateContactForm(self)
		self.btn_new = tk.Button(self, text="Add New Contacts")

		self.list.pack(side=tk.LEFT)
		self.form.pack()
		self.btn_new.pack(padx=10, pady=25, ipadx=10)



	# UserForm မှာရှိတဲ့ Button များ၏ လုပ်ဆောင်ချက်များကို Conrolller နှင့် ချိတ်ဆက်ထား 
	def set_ctrl(self, ctrl):
		# Add New Contacts ခလုတ် လုပ်ဆောင်ချက်အတွက် controller နှင့်ချိတ်ဆက်
		self.btn_new.config(command=ctrl.create_contact) 
		# listbox မှာရှိတဲ့ အချက်အလက် ကို Double Click လုပ်ပြီး အချက်အလက်အသေးစိတ်ကို UserForm တွင် ပြသရန်အတွက် Controller နှင့်ချိတ်ဆက်ထား
		self.list.bind_doble_click(ctrl.select_contact)  
		self.form.bind_save(ctrl.update_contact) # Save Button ခလုတ် လုပ်ဆောင်ချက်အတွက် controller နှင့်ချိတ်ဆက်
		self.form.bind_delete(ctrl.delete_contact)

	def add_contact(self, contact):
		self.list.insert(contact)

	def load_details(self, contact):
		self.form.load_detail(contact)

	def get_details(self):
		return self.form.get_details()

	def update_contact(self, contact, index):
		self.list.update(contact, index)

	def remove_contact(self, index):
		self.form.clear() # UserForm ထဲမှာရှိတဲ့ အချက်အလက်တွေကိုလဲ ဖျက်
		self.list.delete(index) # ListBox ထဲမှာရှိတဲ့ အချက်အလက်တွေကိုလဲ ဖျက်

























