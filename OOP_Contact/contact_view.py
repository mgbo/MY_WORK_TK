
import tkinter as tk
from contact import Contact
from tkinter import messagebox as mb
import csv
import sqlite3


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

		self.labels = [tk.Label(self.frame, text=name) for name in self.field]
		self.entries = [tk.Entry(self.frame) for _ in self.field]
		self.widgets = list(zip(self.labels, self.entries))

		for i, (label, entry) in enumerate(self.widgets):
			label.grid(row=i, column=0, sticky=tk.W)
			entry.grid(row=i, column=1)

		self.frame.pack(expand=1)

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
	def __init__(self, conn):
		super().__init__()
		self.title("CSV Contact List")
		self.conn = conn
		self.selection = None # database table မှ rowid ကိုရယူရန်အတွက်

		self.lb = ContactList(self, height=10) # listbox အတွက်
		# self.frm = ContactForm(self)
		self.frm = UpdateContactForm(self) # ContactForm အတွက်

		self.btn_new = tk.Button(self, text='Add', command=self.add_contact) # add contant form ခလုပ်
		self.contacts =self.load_contacts()


		self.lb.pack(side=tk.LEFT, padx=10, pady=10)
		self.frm.pack(padx=10, pady=10)
		self.btn_new.pack(side=tk.BOTTOM, ipadx=10, padx=10, pady=10)

		# c = Contact('mg', 'mg', 'mgmg@gmail.com', '(789) 8967544') # my example
		# self.frm.load_detail(c)

		for contact in self.contacts:
			# print (contact)
			self.lb.insert(contact)

		self.lb.bind_doble_click(self.show_contact) # doble click ဖြင့် listbox မှ data ကို contactform တွင်ပြ
		self.frm.bind_save(self.update_contact)
		self.frm.bind_delete(self.delete_contact)


	# Contact object အချက်အလက်များကို listbox ထဲသို့ထည့်
	def load_contacts(self):
		# # csv file မှ အချက်အလက်များကို listbox ထဲသို့ထည့်
		# with open('contacts.csv','r') as f:
		# 	return [Contact(*r) for r in csv.reader(f)]

		contacts = []
		sql = """SELECT rowid, last_name, first_name, email, phone FROM contacts"""
		for row in self.conn.execute(sql):
			contact = Contact(*row[1:])
			contact.rowid = row[0]
			contacts.append(contact)
		return contacts

	# listbox ထဲမှာ data ကို index နံပါတ်မှတဆင့် ယူ
	def show_contact(self, index):
		self.selection = index
		contact = self.contacts[index]
		self.frm.load_detail(contact)
	
	def to_values(self, c):
		return (c.last_name, c.first_name, c.email, c.phone)

	def add_contact(self):
		new_contact = NewContact(self)
		contact = new_contact.show()
		print ("Show from NewConatact class", contact)

		if not contact:
			return
		
		values = self.to_values(contact) # Contactform မှရရှိလာသော အချက်အလက် များကို Conatact object အဖြစ်ပြောင်းလဲ
		with self.conn:
			cursor = self.conn.cursor()
			cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", values)
			contact.rowid = cursor.lastrowid
		
		self.contacts.append(contact)
		self.lb.insert(contact)
	
	# Conatact data များ ပြန်လဲ update ပြုလုပ်ခြင်း
	def update_contact(self):
		if self.selection is None:
			return

		rowid = self.contacts[self.selection].rowid
		print ("self.selection :", self.selection)
		print ("Row id :", rowid)

		contact = self.frm.get_details()
		print ("contact :", contact)

		if contact:
			values = self.to_values(contact)

			with self.conn:
				sql = """UPDATE contacts SET last_name=?, first_name=?, email=?, phone=? WHERE rowid = ?"""
				self.conn.execute(sql, values + (rowid,))
				
			contact.rowid = rowid
			self.contacts[self.selection] = contact
			self.lb.update(contact, self.selection) # listbox ထဲသို့ ထည့်သွင်း
	
	def delete_contact(self):
		if self.selection is None:
			return
		rowid = self.contacts[self.selection].rowid # List ထဲမှ Contact object ကို index နံပါတ်မှရယူ

		with self.conn:
			self.conn.execute("DELETE FROM contacts WHERE rowid=?", (rowid,))
		
		self.frm.clear()
		self.lb.delete(self.selection)
		self.selection=None


def main():
	with sqlite3.connect("contacts.db") as conn:
		app = ContactView(conn)
		app.mainloop()


if __name__ == '__main__':
	# app = ContactView()
	# app.mainloop()
	main()



































