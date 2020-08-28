
from tkinter import*
import math, random
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1340x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        #=============== Variables =================
        #================ Cometics ================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        #=============== Gocery ======================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #=============== Cold Drinks ======================
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup= IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #=============== Cold Drinks ======================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax= StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #================== Customer =================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))        
        self.search_bill = StringVar()


        #=========================== Customer Detail Frame =================================
        F1 = LabelFrame(self.root, text="ဝယ်ယူသူအကြောင်း", bd=12, relief=GROOVE, font=("times new roman", 12, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="အမည်", font=("times new roman", 12, "bold"), fg='white', bg=bg_color).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="ဖုန်းနံပါတ်", font=("times new roman", 12, "bold"), fg='white', bg=bg_color).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="ဘောက်ချာနံပါတ်", font=("times new roman", 12, "bold"), fg='white', bg=bg_color).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10)


        #================================ Cometics Frames ====================================
        F2 = LabelFrame(self.root, text="အလှကုန်ပစ္စည်း", bd=10, relief=GROOVE, font=("times new roman", 12, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=170, width=325, height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        bath_txt = Entry(F2, width=10, textvariable=self.soap ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=0, pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=0, pady=10)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        face_w_txt = Entry(F2, width=10, textvariable= self.face_wash,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=0, pady=10)

        hair_s__lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        hari_s_txt = Entry(F2, width=10, textvariable=self.spray ,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=0, pady=10)

        hair_g_lbl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        hair_g_txt = Entry(F2, width=10, textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        body_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        body_txt = Entry(F2, width=10, textvariable=self.loshan, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=0, pady=10)

        #================================ Grocery Frames ====================================
        F3 = LabelFrame(self.root, text="လူသုံးကုန်ပစ္စည်း", bd=10, relief=GROOVE, font=("times new roman", 12, "bold"), fg="gold", bg=bg_color)
        F3.place(x=335, y=170, width=325, height=380)

        Bath_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        Bath_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=0, pady=10)

        Face_cream_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        Face_cream_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=0, pady=10)

        Face_w_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        Face_w_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=0, pady=10)

        hair_s__lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        Hari_s_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=0, pady=10)

        Hair_g_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        Hair_g_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        Body_l__lbl = Label(F3, text="မြေပဲ", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        Body_s_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=0, pady=10)

        #================================ Cold Drink Frames ====================================
        F4 = LabelFrame(self.root, text="အအေးမျိုးစုံ", bd=10, relief=GROOVE, font=("times new roman", 12, "bold"), fg="gold", bg=bg_color)
        F4.place(x=665, y=170, width=325, height=380)

        Bath_lbl = Label(F4, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        Bath_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=0, pady=10)

        Face_cream_lbl = Label(F4, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        Face_cream_txt = Entry(F4, width=10, textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=0, pady=10)

        Face_w_lbl = Label(F4, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        Face_w_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=0, pady=10)

        hair_s__lbl = Label(F4, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        Hari_s_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=0, pady=10)

        Hair_g_lbl = Label(F4, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        Hair_g_txt = Entry(F4, width=10, textvariable=self.sprite,  font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        Body_l__lbl = Label(F4, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        Body_s_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=0, pady=10)


        #================ Bill Area ============================================================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000, y=170, width=340, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #============================= Button Frame =============================================
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_label = Label(F6, text='အလှကုန်ကျသင့်ငွေ', font=("times new roman", 10, "bold"), bg=bg_color, fg="white").grid(row=0, column=0, padx=25)
        m1_txt = Entry(F6, textvariable=self.cosmetic_price, width=18, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=1)

        m2_label = Label(F6, text='လူသုံးကုန်ကျသင်ငွေ', font=("times new roman", 10, "bold"), bg=bg_color, fg="white").grid(row=1, column=0, padx=5)
        m2_txt = Entry(F6, textvariable=self.grocery_price, width=18, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=1)

        m3_label = Label(F6, text='အအေးကျသင့်ငွေ', font=("times new roman", 10, "bold"), bg=bg_color, fg="white").grid(row=2, column=0, padx=5)
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1)



        c1_label = Label(F6, text='အလှကုန်အခွန်', font=("times new roman", 10, "bold"), bg=bg_color, fg="white").grid(row=0, column=2, padx=25)
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=3)

        c2_label = Label(F6, text='လူသုံးကုန်အခွန်', font=("times new roman", 10, "bold"), bg=bg_color, fg="white").grid(row=1, column=2, padx=5)
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=3)

        c3_label = Label(F6, text='အအေးအခွန်', font=("times new roman", 10, "bold"), bg=bg_color, fg="white").grid(row=2, column=2, padx=5)
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=3)

        #------------------- Button Frame right ---------------------------------
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=670, width=650, height=105)

        total_btn = Button(btn_f, command= self.total, text="Total", bg='cadetblue', fg='white', bd=2, pady=15, width=11, font='arial 13 bold').grid(row=0, column=0, padx=5, pady=5)
        Gbill_btn = Button(btn_f, text="Genrate", command=self.bill_area, bg='cadetblue', fg='white', bd=2, pady=15, width=11, font='arial 13 bold').grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn_f, text="Clear", command=self.clear, bg='cadetblue', fg='white', bd=2, pady=15, width=11, font='arial 13 bold').grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_f, text="Exit", command=self.exit, bg='cadetblue', fg='white', bd=2, pady=15, width=11, font='arial 13 bold').grid(row=0, column=3, padx=5, pady=5)


        #================================ Bill Area ===========================================
        self.welcome_bill()

    def total(self):
        #================== for cosmetic category ===========================
        self.total_cosmetic_price = (
                                        (self.soap.get()*40)+
                                        (self.face_cream.get()*40)+
                                        (self.face_wash.get()*60)+
                                        (self.gell.get()*180)+
                                        (self.loshan.get()*180)

        )
        self.cosmetic_price.set(str(self.total_cosmetic_price) + " ကျပ်")
        self.cosmetic_tax.set(str(self.total_cosmetic_price*0.05)+ " ကျပ်")


        #================== for cosmetic category ===========================
        self.total_grocery_price = (
                                        (self.rice.get()*40)+
                                        (self.food_oil.get()*40)+
                                        (self.daal.get()*60)+
                                        (self.sugar.get()*180)+
                                        (self.tea.get()*180)

        )
        self.grocery_price.set(str(self.total_grocery_price) +  " ကျပ်")
        self.grocery_tax.set(str(self.total_grocery_price*0.3)+ " ကျပ်")

        #================== for cold drink category ===========================
        self.total_drink_price = (
                                        (self.maza.get()*40)+
                                        (self.cock.get()*40)+
                                        (self.thumbsup.get()*60)+
                                        (self.frooti.get()*180)+
                                        (self.limca.get()*180)

        )
        self.cold_drink_price.set(str(self.total_drink_price)+ " ကျပ်")
        # self.cold_drink_tax.set(str(round((self.total_drink_price)*0.01),2) + " ကျပ်")
        self.cold_drink_tax.set(str(round(self.total_drink_price*0.05,2)) + " ကျပ်")

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome MDOLGORU Reatil")
        self.txtarea.insert(END, f"\nBill No: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n=====================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END, "\n=====================================")
    
    def bill_area(self):
        self.welcome_bill()
        if self.soap.get() !=0:
            self.txtarea.insert(END, f"\n ရေချိုးဆပ်ပြာ\t\t{self.soap.get()}\t\t{self.soap.get() * 40}")

        if self.face_cream.get() !=0:
            self.txtarea.insert(END, f"\n မျက်နှာလိမ်ဆေး\t\t{self.face_cream.get()}\t\t{self.face_cream.get()*100}")
        
        if self.face_wash.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.face_wash.get()}\t\t{self.face_wash.get() * 200}")
        
        if self.spray.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.spray.get()}\t\t{self.spray.get() * 80}")

        if self.gell.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.gell.get()}\t\t{self.gell.get() * 70}")
        
        if self.loshan.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.loshan.get()}\t\t{self.loshan.get() * 500}")
        
        if self.soap.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

        if self.soap.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        
        if self.soap.get() !=0:
            self.txtarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

    #Function to clear the bill area
    def clear(self):
        self.txtarea.delete('1.0',END)
    
    
    #Function to exit
    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()









