

from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk

# ------------- database libary --------------
import pymysql
import mysql.connector

import pandas

from PIL import Image
import time
import random

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)

def IntroLabelTick():
    global count, text
    # print (count)
    if (count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count +=1
        
    SliderLabel.after(200, IntroLabelTick)

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y   ")
    clock.config(text='   Date : '+ date_string + '\n' + 'Time : ' + time_string)
    clock.after(200, tick)

def add_student():
    def add_submit():
        id = id_val.get() 
        name = name_val.get() 
        mobile = mobile_val.get() 
        email = email_val.get() 
        address = address_val.get() 
        gender = gender_val.get() 
        dob = dob_val.get()
        added_date = time.strftime("%d/%m/%Y")
        added_time = time.strftime("%H:%M:%S")

        # print (added_date)
        # print (added_time)

        try:
            strr = 'insert into studentdata values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, added_date, added_time))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id {} {} Added sucessfully.. and want to clean the form'.format(id,name), parent=add_root)

            if (res==True):
                id_val.set('')
                name_val.set('')
                mobile_val.set('')
                email_val.set('')
                address_val.set('')
                gender_val.set('')
                dob_val.set('')
        except:
            messagebox.showerror('Notifications', 'Id Already Exit try another id...')

        #------- select database table --------------
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        # print (strr)
        datas = mycursor.fetchall()
        # print (datas)
        student_table.delete(*student_table.get_children())

        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            # print (vv)
            student_table.insert('', END, value=vv)




    # print ('student added')
    add_root = Toplevel(master=DataEntryFrame)
    add_root.grab_set()
    add_root.geometry('470x470+220+200')
    add_root.title('Student Management System')
    add_root.config(bg='blue')
    # add_root.iconbitmap(r'C:\Users\naylintun\Desktop\S_M_system\mana.ico')
    add_root.resizable(False, False)

    #---------------------- add student label ----------------------
    id_label = Label(add_root, text='Enter Id : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    id_label.place(x=10, y=10)

    name_label = Label(add_root, text='Enter Name : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)

    mobile_label = Label(add_root, text='Enter Mobile : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobile_label.place(x=10, y=130)

    email_label = Label(add_root, text='Enter Email : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    email_label.place(x=10, y=190)

    address_label = Label(add_root, text='Enter Address : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    address_label.place(x=10, y=250)

    gender_label = Label(add_root, text='Enter Gender : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    gender_label.place(x=10, y=310)

    dob_label = Label(add_root, text='Enter D.O.B : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=370)

    #---------------------- add student label ----------------------
    id_val = StringVar()
    name_val = StringVar()
    mobile_val = StringVar()
    email_val = StringVar()
    address_val = StringVar()
    gender_val = StringVar()
    dob_val = StringVar()


    id_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=id_val)
    id_entry.place(x=250, y=10)

    name_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=name_val)
    name_entry.place(x=250, y=70)

    mobile_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=mobile_val)
    mobile_entry.place(x=250, y=130)

    email_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=email_val)
    email_entry.place(x=250, y=190)

    address_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=address_val)
    address_entry.place(x=250, y=250)

    gender_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=gender_val)
    gender_entry.place(x=250, y=310)

    dob_entry = Entry(add_root, font=('roman', 15, 'bold'), bd=5, textvariable=dob_val)
    dob_entry.place(x=250, y=370)

    #---------------------- add button ---------------
    submit_btn = Button(add_root, text='Submit', command=add_submit, font=('roman', 15, 'bold'), width=20, bd=5,\
        activebackground='blue', activeforeground='white')
    submit_btn.place(x=150, y=420)


    add_root.mainloop()

def search_student():
    def search():
        id = id_val.get() 
        name = name_val.get() 
        mobile = mobile_val.get() 
        email = email_val.get() 
        address = address_val.get() 
        gender = gender_val.get() 
        dob = dob_val.get()
        date = date_val.get()
        # print (date_val, type(date_val))
        # added_time = time.strftime("%H:%M:%S")
        
        if (id != ''):
            strr = 'select *from studentdata where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)
        
        elif (name != ''):
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)

        elif (mobile != ''):
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)

        elif (email != ''):
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)

        elif (address != ''):
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)

        elif (gender != ''):
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)


        elif (dob != ''):
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)

        elif (date != ''):
            strr = 'select *from studentdata where date=%s'
            mycursor.execute(strr, (date))
            datas = mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # print (vv)
                student_table.insert('', END, value=vv)

    # print ('student added')
    search_root = Toplevel(master=DataEntryFrame)
    search_root.grab_set()
    search_root.geometry('470x540+220+200')
    search_root.title('Student Management System')
    search_root.config(bg='blue')
    # search_root.iconbitmap(r'C:\Users\naylintun\Desktop\S_M_system\mana.ico')
    search_root.resizable(False, False)

    #---------------------- add student label ----------------------
    id_label = Label(search_root, text='Enter Id : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    id_label.place(x=10, y=10)

    name_label = Label(search_root, text='Enter Name : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)

    mobile_label = Label(search_root, text='Enter Mobile : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobile_label.place(x=10, y=130)

    email_label = Label(search_root, text='Enter Email : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    email_label.place(x=10, y=190)

    address_label = Label(search_root, text='Enter Address : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    address_label.place(x=10, y=250)

    gender_label = Label(search_root, text='Enter Gender : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    gender_label.place(x=10, y=310)

    dob_label = Label(search_root, text='Enter D.O.B : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=370)

    dob_label = Label(search_root, text='Date : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=430)

    #---------------------- add student label ----------------------
    id_val = StringVar()
    name_val = StringVar()
    mobile_val = StringVar()
    email_val = StringVar()
    address_val = StringVar()
    gender_val = StringVar()
    dob_val = StringVar()
    date_val = StringVar()

    id_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=id_val)
    id_entry.place(x=250, y=10)

    name_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=name_val)
    name_entry.place(x=250, y=70)

    mobile_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=mobile_val)
    mobile_entry.place(x=250, y=130)

    email_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=email_val)
    email_entry.place(x=250, y=190)

    address_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=address_val)
    address_entry.place(x=250, y=250)

    gender_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=gender_val)
    gender_entry.place(x=250, y=310)

    dob_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=dob_val)
    dob_entry.place(x=250, y=370)

    date_entry = Entry(search_root, font=('roman', 15, 'bold'), bd=5, textvariable=date_val)
    date_entry.place(x=250, y=430)

    #---------------------- add button ---------------
    submit_btn = Button(search_root, text='Submit', command=search, font=('roman', 15, 'bold'), width=20, bd=5,\
        activebackground='blue', activeforeground='white')
    submit_btn.place(x=150, y=480)


    search_root.mainloop()


def del_student():

    #------------ for selecting from ui table (TreeView) -------------------
    cc = student_table.focus()
    content = student_table.item(cc)
    # print (content)

    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted sucessfully..'.format(pp))

    #======== show all data after deleting ========================
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        # print (vv)
        student_table.insert('', END, value=vv)



def update_student():
    def update():
        id = id_val.get() 
        name = name_val.get() 
        mobile = mobile_val.get() 
        email = email_val.get() 
        address = address_val.get() 
        gender = gender_val.get() 
        dob = dob_val.get()
        t_date = date_val.get()
        time = time_val.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, t_date, time, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} has been updated...'.format(id), parent=update_root)


        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas= mycursor.fetchall()

        student_table.delete(*student_table.get_children())

        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            student_table.insert('', END, values=vv)

    # print ('student added')
    update_root = Toplevel(master=DataEntryFrame)
    update_root.grab_set()
    update_root.geometry('470x585+220+160')
    update_root.title('Student Management System')
    update_root.config(bg='blue')
    # update_root.iconbitmap(r'C:\Users\naylintun\Desktop\S_M_system\mana.ico')
    update_root.resizable(False, False)

    #---------------------- add student label ----------------------
    id_label = Label(update_root, text='Enter Id : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    id_label.place(x=10, y=10)

    name_label = Label(update_root, text='Enter Name : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)

    mobile_label = Label(update_root, text='Enter Mobile : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobile_label.place(x=10, y=130)

    email_label = Label(update_root, text='Enter Email : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    email_label.place(x=10, y=190)

    address_label = Label(update_root, text='Enter Address : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    address_label.place(x=10, y=250)

    gender_label = Label(update_root, text='Enter Gender : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    gender_label.place(x=10, y=310)

    dob_label = Label(update_root, text='Enter D.O.B : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=370)

    dob_label = Label(update_root, text='Date : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=430)

    time_label = Label(update_root, text='Time : ', bg='gold2', font=('times', 20, 'bold'), \
    relief=GROOVE, borderwidth=3, width=12, anchor='w')
    time_label.place(x=10, y=490)

    #---------------------- add student label ----------------------
    id_val = StringVar()
    name_val = StringVar()
    mobile_val = StringVar()
    email_val = StringVar()
    address_val = StringVar()
    gender_val = StringVar()
    dob_val = StringVar()
    date_val = StringVar()
    time_val = StringVar()

    id_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=id_val)
    id_entry.place(x=250, y=10)

    name_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=name_val)
    name_entry.place(x=250, y=70)

    mobile_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=mobile_val)
    mobile_entry.place(x=250, y=130)

    email_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=email_val)
    email_entry.place(x=250, y=190)

    address_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=address_val)
    address_entry.place(x=250, y=250)

    gender_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=gender_val)
    gender_entry.place(x=250, y=310)

    dob_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=dob_val)
    dob_entry.place(x=250, y=370)

    date_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=date_val)
    date_entry.place(x=250, y=430)

    time_entry = Entry(update_root, font=('roman', 15, 'bold'), bd=5, textvariable=time_val)
    time_entry.place(x=250, y=490)

    #---------------------- add button ---------------
    submit_btn = Button(update_root, text='Submit', command=update, font=('roman', 15, 'bold'), width=20, bd=5,\
        activebackground='blue', activeforeground='white')
    submit_btn.place(x=150, y=530)

    cc = student_table.focus()
    content = student_table.item(cc)
    pp = content['values']

    if (len(pp) != 0 ):
        id_val.set(pp[0])
        name_val.set(pp[1])
        mobile_val.set(pp[2])
        email_val.set(pp[3])
        address_val.set(pp[4])
        gender_val.set(pp[5])
        dob_val.set(pp[6])
        date_val.set(pp[7])
        time_val.set(pp[8])

    update_root.mainloop()

def show_student():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas= mycursor.fetchall()

    student_table.delete(*student_table.get_children())

    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        student_table.insert('', END, values=vv)

def export_student():
    ff = filedialog.asksaveasfilename()
    gg = student_table.get_children()
    id, name, mobile, email, address, gender, dob, date, time = [], [], [], [], [], [], [], [], []

    for i in gg:
        content = student_table.item(i)
        pp = content['values']
        # id.append(pp[0])
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]), \
            gender.append(pp[5]), dob.append(pp[6]), date.append(pp[7]), time.append(pp[8])

    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'DOB', 'Added Date', 'Added Time']

    df = pandas.DataFrame(list(zip(id, name, mobile, email, address, gender, dob, date, time)), columns=dd)

    paths = r'{}.csv'.format(ff)

    df.to_csv(paths, index=False)

    messagebox.showinfo('Notifications', 'Student data is saved {}'.format(paths))

def exit_student():
    res = messagebox.askyesno('Notification', 'Do you want to exit?')

    if res == True:
        root.destroy()

###################################### Connnection of Database ######################################################
def Connect_db():
    def submit_db():
        global con, mycursor

        host = host_val.get()
        user = user_val.get()
        password = password_val.get()
        print (host, user, password)

        # host = 'localhost'
        # user = 'root'
        # password = 'root'

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
            print ('connected!!')
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again!', parent=db_root)
            return

        try:
            strr = 'create database my_student_1'
            mycursor.execute(strr)
            strr = 'use my_student_1'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int, name varchar(20), mobile varchar(12), email varchar(30),address varchar(100), gender varchar(50), dob varchar(50), date varchar(50), time varchar(50))'
            mycursor.execute(strr)

            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'database created and now you are connected to the database ........', parent=db_root)

        except:
            strr = 'use my_student_1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ........', parent=db_root)
        
        db_root.destroy()


    db_root = Toplevel()
    db_root.grab_set()
    db_root.geometry('470x250+800+330')
    # db_root.iconbitmap(r'C:\Users\naylintun\Desktop\S_M_system\mana.ico')
    db_root.resizable(False, False)
    db_root.config(bg='blue')

    #------------------------ Connection Labels ------------------
    host_label = Label(db_root, text='Enter Host', bg='gold2', font=('times', 20, 'bold'),\
        relief=GROOVE, borderwidth=3, width=12, anchor='w')
    host_label.place(x=10, y=10)

    name_label = Label(db_root, text='Enter User', bg='gold2', font=('times', 20, 'bold'),\
        relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)

    password_label = Label(db_root, text='Enter Password', bg='gold2', font=('times', 20, 'bold'),\
        relief=GROOVE, borderwidth=3, width=12, anchor='w')
    password_label.place(x=10, y=130)

    #============================ Connectdb Entry =========================
    host_val = StringVar()
    user_val = StringVar()
    password_val = StringVar()

    host_entry = Entry(db_root, font=('roman', 15, 'bold'), bd=5, textvariable=host_val)
    host_entry.place(x=250, y=10)

    host_entry = Entry(db_root, font=('roman', 15, 'bold'), bd=5, textvariable=user_val)
    host_entry.place(x=250, y=70)

    host_entry = Entry(db_root, font=('roman', 15, 'bold'), bd=5, show='*', textvariable=password_val)
    host_entry.place(x=250, y=130)

    #========================= connect db button ===============================
    submit_button = Button(db_root, text='Submit', command=submit_db, font=('roman', 15, 'bold'), width=20,\
        activebackground='blue', activeforeground='white')
    submit_button.place(x=150, y=180)

    # db_root.mainloop()
    # db_root.after(5000, lambda: db_root.destroy())


#############################################################################################
root = Tk()
root.title('Student Management system')
root.config(bg='gold2')
root.geometry("1174x700+200+200")

# root.iconbitmap(r'C:\Users\naylintun\Desktop\S_M_system\mana.ico')
root.resizable(False, False)

##################################### All Frame ( အဝင်နှင့် အထွက်) #########################################
DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=6)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

#============================== Data entry Frame (All button ) ======================
welcome_txt = '---------------- Welcome --------------'
front_label = Label(DataEntryFrame, text=welcome_txt, font=("arial", 22, 'italic bold'), \
    bg='gold2')
front_label.pack(side=TOP, expand=True)

add_btn = Button(DataEntryFrame, text="1. add student", command=add_student, width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
add_btn.pack(side=TOP, expand=True)

search_btn = Button(DataEntryFrame, command=search_student, text="2. Search student", width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
search_btn.pack(side=TOP, expand=True)

del_btn = Button(DataEntryFrame, command=del_student, text="3. Delete student", width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
del_btn.pack(side=TOP, expand=True)

update_btn = Button(DataEntryFrame, command=update_student, text="4. Update student", width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
update_btn.pack(side=TOP, expand=True)

show_btn = Button(DataEntryFrame, command=show_student, text="5. Show student", width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
show_btn.pack(side=TOP, expand=True)

export_btn = Button(DataEntryFrame, command= export_student, text="6. Export Data", width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
export_btn.pack(side=TOP, expand=True)

exit_btn = Button(DataEntryFrame, text="7. Exit", command=exit_student, width=25, font=("chiller", 25, 'bold'), \
    bg='skyblue3', bd=6, relief=RIDGE, borderwidth=5)
exit_btn.pack(side=TOP, expand=True)



#================= show all data frame (Table Frame) =============================
ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=600)


#-------------------- Showe data frame --------------------
style = ttk.Style()
style.configure('Treeview.Heaing', font=('chiller', 18, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 12), foreground='black')

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)

student_table = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No.', 'Email', 'Address', 'Gender','D.O.B', 'Added Date', 'Added Time' ), \
    yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading('Id', text='Id')
student_table.heading('Name', text='Name')
student_table.heading('Mobile No.', text='Mobile No.')
student_table.heading('Email', text='Email')
student_table.heading('Address', text='Address')
student_table.heading('Gender', text='Gender')
student_table.heading('D.O.B', text='DOB')
student_table.heading('Added Date', text='Added Date')
student_table.heading('Added Time', text='Add time')

student_table['show'] = 'headings'


student_table.column('Id', width=100)
student_table.column('Name', width=200)
student_table.column('Mobile No.', width=200)
student_table.column('Email', width=300)
student_table.column('Address', width=300)
student_table.column('Gender', width=100)
student_table.column('D.O.B', width=150)
student_table.column('Added Date', width=150)
student_table.column('Added Time', width=150)

student_table.pack(fill=BOTH, expand=1)




######################################## Title and Label #################################################
ss = "Student Management System "
text=''
count = 0
SliderLabel = Label(root, text=text,\
font=('chiller', 30, "bold"), bg='cyan', borderwidth=4, relief=RAISED, width=35)
SliderLabel.place(x=260, y=0)
IntroLabelTick()
# IntroLabelColorTick()


#################################### Date and Clock ###################################################
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=3, \
    width=20, bg='lawn green')
clock.place(x=0, y=0)
tick()

####################################### Connect to Database Button  ##################################################
connect_button = Button(root, text='Connect To Database', command=Connect_db, width=23, bd=6, relief=RIDGE, \
    font=('chiller', 19, 'bold'), bg='green2')
connect_button.place(x=920, y=0)

root.mainloop()

# CREATE TABLE `studentmanagesystem`.`studentdata` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `name` VARCHAR(50) NULL,
#   `mobile` VARCHAR(45) NULL,
#   `email` VARCHAR(45) NULL,
#   `address` VARCHAR(45) NULL,
#   `gender` VARCHAR(45) NULL,
#   `dob` VARCHAR(45) NULL,
#   `date` VARCHAR(45) NULL,
#   `time` VARCHAR(45) NULL,
#   PRIMARY KEY (`id`));
