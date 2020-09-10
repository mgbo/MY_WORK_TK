
import tkinter as tk
from contact import Contact
from tkinter import messagebox as mb
import csv


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


class  ContactForm(tk.LabelFrame):
	field = ('Last Name', 'First Name', 'Email', 'Phone')

	def __init__(self, master, **kwargs):
		super().__init__(master, text='Contact', padx=10, pady=10, **kwargs)
		self.frame = tk.Frame(self)

		self.labels = [tk.Label(self.frame, text=name) for name in self.field]
		self.entries = [tk.Entry(self.frame) for _ in self.field]
		self.widgets = list(zip(self.labels, self.entries))

		for i, (label, entry) in enumerate(self.widgets):
			label.grid(row=i, column=0, sticky=tk.W)
			entry.grid(row=i, column=1)

		self.frame.pack()

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



class ContactView(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("CSV Contact List")

		self.lb = ContactList(self, height=10)
		self.frm = ContactForm(self)
		self.contacts =self.load_contacts()

		self.lb.pack(side=tk.LEFT, padx=10, pady=10)
		self.frm.pack(side=tk.LEFT, padx=10, pady=10)

		# c = Contact('mg', 'mg', 'mgmg@gmail.com', '(789) 8967544') # my example
		# self.frm.load_detail(c)

		for contact in self.contacts:
			print (contact)
			self.lb.insert(contact)

		self.lb.bind_doble_click(self.show_contact)

	# csv file မှ အချက်အလက်များကို listbox ထဲသို့ထည့်
	def load_contacts(self):
		with open('contacts.csv','r') as f:
			return [Contact(*r) for r in csv.reader(f)]

	# listbox ထဲမှာ data ကို index မှတဆင့်ယူ
	def show_contact(self, index):
		contact = self.contacts[index]
		self.frm.load_detail(contact)



if __name__ == '__main__':
	app = ContactView()
	app.mainloop()



























