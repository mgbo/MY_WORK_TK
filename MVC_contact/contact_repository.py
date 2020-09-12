
import tkinter as tk
from contact import Contact
import sqlite3

class ContactRepository:
	def __init__(self, conn):
		self.conn = conn

	def to_values(self, c): # Contact object မှ value များကိုရယူရန်
		return c.last_name, c.first_name, c.email, c.phone

	def get_contacts(self):
		sql = "SELECT rowid, last_name, first_name, email, phone FROM contacts"

		for row in self.conn.execute(sql):
			contact = Contact(*row[1:])
			contact.rowid = row[0]
			yield contact

	def add_contact(self, contact):
		sql = "INSERT INTO contacts VALUES(?,?,?,?)"

		with self.conn:
			cursor = self.conn.cursor()
			cursor.execute(sql, self.to_values(contact))
			contact.rowid = cursor.lastrowid # နောက်ဆုံး rowid နံပါတ်ပေးရန်အတွက်
			print ('Contact.rowid :', contact.rowid)

		return contact

	def update_contact(self, contact):
		rowid = contact.rowid

		sql ="UPDATE contacts SET last_name=?, first_name=?, email=?, phone=? WHERE rowid=?"

		with self.conn:
			self.conn.execute(sql, self.to_values(contact)+(rowid,))

		return contact

	def delete_contact(self, contact):
		sql = "DELETE FROM contacts WHERE rowid = ?"

		with self.conn:
			self.conn.execute(sql, (contact.rowid,))

















