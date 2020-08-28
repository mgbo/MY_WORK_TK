
from tkinter import*

root = Tk()
root.geometry("200x200")

# Button(bg='red').place(x=75, y=20)
# Button(bg='green').place(relx=0.5, rely=0.5)

Label(bg='green').place(x=10, y=10, width=50, height=30)

Label(bg='lightgreen').place(x=0, y=70, relwidth=0.5, relheight=0.15)


root.mainloop()