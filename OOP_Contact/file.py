
from contact import Contact

with open('contacts.txt', 'r') as f:
    for i in f:
        i = i.split(',')
        print (*i)
        print(Contact(*i))
