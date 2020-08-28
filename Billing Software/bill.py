
from tkinter import*

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x720+0+0")
        self.root.title("Billing Software")

        #========================== color variable =====================================================
        bg_color = "#074463"
        lbl_color = 'white'
        fg_color = "white"


        #============================ variable ======================
        self.seconds = 0

        #============================== App Title =========================================================
        title = Label(self.root, text="Billing Software",bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        #=========================== Customer Detail Frame =================================
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", font=("times new roman", 18, "bold"), fg='white', bg=bg_color).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cname_lbl = Label(F1, text="Phone No.", font=("times new roman", 18, "bold"), fg='white', bg=bg_color).grid(row=0, column=2, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cname_lbl = Label(F1, text="Bill Number", font=("times new roman", 18, "bold"), fg='white', bg=bg_color).grid(row=0, column=4, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        # bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10)

        self.timer = Label(F1, text="0 s", font="Arial 30", width=7, bd=5, relief=SOLID, highlightcolor='green')
        self.timer.grid(row=0, column=6, padx=10)
        self.refresh_label()


        #================================ Cometics Frames ====================================
        F2 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=170, width=325, height=380)

        Bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        Bath_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=0, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        Face_cream_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=0, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        Face_w_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=0, pady=10)

        hair_s__lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        Hari_s_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=0, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        Hair_g_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        Body_l__lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        Body_s_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=0, pady=10)

        #================================ Cometics Frames ====================================
        F3 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=170, width=325, height=380)

        Bath_lbl = Label(F3, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        Bath_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=0, pady=10)

        Face_cream_lbl = Label(F3, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        Face_cream_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=0, pady=10)

        Face_w_lbl = Label(F3, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        Face_w_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=0, pady=10)

        hair_s__lbl = Label(F3, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        Hari_s_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=0, pady=10)

        Hair_g_lbl = Label(F3, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        Hair_g_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        Body_l__lbl = Label(F3, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        Body_s_txt = Entry(F3, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=0, pady=10)

        #================================ Cold Drink Frames ====================================
        F4 = LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=670, y=170, width=325, height=380)

        Bath_lbl = Label(F4, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="W")
        Bath_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=0, pady=10)

        Face_cream_lbl = Label(F4, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="W")
        Face_cream_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=0, pady=10)

        Face_w_lbl = Label(F4, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="W")
        Face_w_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=0, pady=10)

        hair_s__lbl = Label(F4, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="W")
        Hari_s_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=0, pady=10)

        Hair_g_lbl = Label(F4, text="Hair Gell", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="W")
        Hair_g_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=0, pady=10)

        Body_l__lbl = Label(F4, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="W")
        Body_s_txt = Entry(F4, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=0, pady=10)


        #================ Bill Area ====================================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=170, width=340, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #============================= Button Frame =============================
        F6 = LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=160)

        #===================
        cosm_lbl = Label(F6,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F6,bd = 8,relief = GROOVE)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F6,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F6,bd = 8,relief = GROOVE)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F6,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F6,bd = 8,relief = GROOVE)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F6,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cosmetics Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F6,bd = 8,relief = GROOVE)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F6,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F6,bd = 8,relief = GROOVE)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F6,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 2)
        otht_en = Entry(F6,bd = 8,relief = GROOVE)
        otht_en.grid(row = 2,column = 3,ipady = 5,ipadx = 5)

        #====================
        total_btn = Button(F6,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F6,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F6,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F6,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)





    # ============================= Timer Function =====================
    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        self.seconds += 1
        # display the new time
        self.timer.configure(text="%i s" % self.seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        self.timer.after(1000, self.refresh_label)



if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()