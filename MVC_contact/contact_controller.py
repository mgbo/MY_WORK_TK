

from contact_view import NewContact

class ContactsController:
	def __init__(self, repo, view):
		self.repo = repo
		self.view = view
		self.selection = None
		self.contats = list(repo.get_contacts())


	def start(self):
		for c in self.contats:
			self.view.add_contact(c)

		self.view.mainloop()

	def create_contact(self):
		new_contact = NewContact(self.view).show()
		
		if new_contact:
			contact = self.repo.add_contact(new_contact)
			self.contats.append(contact)
			self.view.add_contact(contact)