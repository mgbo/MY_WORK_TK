

root = Tk()
canvas= Canvas(root, width=100, height=100)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()