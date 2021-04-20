# Pet Shop Application
# Acts like a mini inventory system

'''
Import
Class
--add
--remove
--save
--load
Main
Test
'''

#import
import json
import os.path

# Inventory class
class Inventory:
    pets = {}

    def __init__(self):
        self.load()


    def add(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
            self.pets[key] = q
        print (f"Added")

    def remove(self):
        pass

    def display(self):
        pass

    def save(self):
        pass

    def load(self):
        pass




