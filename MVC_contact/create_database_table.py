import csv
import sqlite3

"""
  database တည်ဆောက်ခြင်းနှင့်
  database ထဲသို့ csv ဖိုင်မှ အချက်အလက်များ ထည့်သွင်းခြင်း
"""
# open("contacts.csv", encoding="utf-8", newline="") as f, \

def main():
	with sqlite3.connect("contacts.db") as conn: # contacts အမည်နှင့် database ထဲတွင် data table တည်ဆောက်ခြင်း
		conn.execute("""CREATE TABLE contacts (
						  last_name text,
						  first_name text,
						  email text,
						  phone text
						)""")
		
		# # csv file မှ အချက်အလက်များကို database သို့ထည့်
		# conn.executemany("INSERT INTO contacts VALUES (?,?,?,?)",
		#                  csv.reader(f))

if __name__ == "__main__":
	main()