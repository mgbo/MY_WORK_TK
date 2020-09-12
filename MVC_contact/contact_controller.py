

from contact_view import NewContact

class ContactsController:
	def __init__(self, repo, view):
		self.repo = repo
		self.view = view
		self.selection = None
		self.contacts= list(repo.get_contacts())


	def start(self):
		for c in self.contacts:
			self.view.add_contact(c) # database ထဲမှာရှိတဲ့ အချက်အလက်များကို listbox ထဲထည့်သွင်း
		self.view.mainloop()

	def create_contact(self): # UserForm မှတစ်ဆင့် new_contact ပြုလုပ်ရန်အတွက်
		new_contact = NewContact(self.view).show()
		print ('New Contact :', new_contact)
		
		if new_contact:
			contact = self.repo.add_contact(new_contact)
			self.contacts.append(contact)
			self.view.add_contact(contact)

	# listbox မှ အချက်အလုပ် ကို double click လုပ်ယုံဖြင့် Contactform တွင် ၎င်းနှင့် ဆိုင်သော အချက်အလက်များပေါ်ရန်
	def select_contact(self, index): 
		self.selection = index
		contact = self.contacts[index]
		print ("Contact : ", contact)
		self.view.load_details(contact)

	def update_contact(self):
		if not self.selection:
			return

		rowid = self.contacts[self.selection].rowid
		print ("Updat Contact Controller : ", rowid)
		update_contact = self.view.get_details()
		update_contact.rowid = rowid
		contact = self.repo.update_contact(update_contact)
		self.contacts[self.selection] = contact
		self.view.update_contact(contact, self.selection)

	def delete_contact(self):
		if not self.selection:
			return

		contact = self.contacts[self.selection]
		print ("Delete_contact :", contact)
		self.repo.delete_contact(contact) # delete data from database
		print ("Delete_contact : DataBase is all ok!!!")
		self.view.remove_contact(self.selection) # delete data from GUI view














