
import sqlite3
from contact_repository import ContactRepository
from contact_view import ContactView
from contact_controller import ContactsController


def main():
    with sqlite3.connect("contacts.db") as conn:
        repo = ContactRepository(conn) # model
        view = ContactView() # view
        ctrl = ContactsController(repo, view) # controller

        view.set_ctrl(ctrl)
        ctrl.start()

if __name__ == "__main__":
    main()
