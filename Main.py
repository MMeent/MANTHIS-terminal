from tkinter import *
root = Tk(screenName="Name", baseName="Name", className="Name")
root.resizable = TRUE
SCREENWIDTH = 1024
SCREENHEIGHT = 720
#test = Frame(root, bg="red", width=100, height=100).pack(side=LEFT)

#frame = Frame(root, width=screenWidth, height=screenHeight, bg="yellow").grid()
#textFrame = Frame(root, width=screenWidth/3, height=screenHeight, bg="", colormap="new").pack()
#buttonFrame = Frame(frame).pack(anchor=E)

boughtItemList = Frame(root, width=(SCREENWIDTH / 3), height=SCREENHEIGHT, bg="red")
boughtItemList.grid(column=0, row=0, rowspan=2)
sellingItemList = Frame(root, width=(SCREENWIDTH / 3 * 2), height=(SCREENHEIGHT - 100), bg="green")
sellingItemList.grid(column=1, row=0, columnspan=2)
calculator = Frame(root, width=(SCREENWIDTH / 3 * 2), height=100, bg="blue")
calculator.grid(column=1, row=1, columnspan=2)

itemList = Text(boughtItemList, width=SCREENWIDTH/3, height=(2*SCREENHEIGHT/3))
"""
button1 = Button(boughtItemList, text="button1", borderwidth=10, relief=FLAT)
button1.pack()
button2 = Button(sellingItemList, text="button2", borderwidth=10, relief=FLAT)
button2.grid(column=0, row=0)
button3 = Button(calculator, text="button3", borderwidth=10, relief=FLAT)
button3.grid(column=0, row=0)
"""
#itemList = Text(frame).grid(column=0, row=1)

bottomBar = Frame(root, width=SCREENWIDTH, height=40, bg="black")
bottomBar.grid(column=0, row=2, columnspan=3)
status = Label(bottomBar, text="Waiting for action", bd=1, relief=SUNKEN).pack(fill=Y)

root.mainloop()