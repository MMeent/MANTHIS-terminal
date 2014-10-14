from tkinter import *
from Terminal.BuyingList import BuyingList

root = Tk(screenName="Name", baseName="Name", className="Name")
root.buying_list = BuyingList()
root.resizable(width=FALSE, height=FALSE)
screenWidth = 1024
screenHeight = 720
root.geometry('{}x{}'.format(screenWidth, screenHeight))
buttonSize = 300
currentAantal = 26


""" vormt en plaatst de drie grote frames die scherm opdelen"""
#oderFrame komt alles in wat met de info van de bestelling te maken heeft
orderFrame = Frame(root, width=(screenWidth / 3), height=screenHeight, bg="red")
orderFrame.grid(column=0, row=0, rowspan=2)
orderFrame.grid_propagate(False)
#komen alle items in te staan (de artikelen)
itemFrame = Frame(root, width=(screenWidth / 3 * 2), height=(screenHeight - 100), bg="green")
itemFrame.grid(column=1, row=0, columnspan=2)
itemFrame.grid_propagate(False)
#overigFrame komt alle andere functionaliteiten in
overigFrame = Frame(root, width=(screenWidth / 3 * 2), height=100, bg="blue")
overigFrame.grid(column=1, row=1, columnspan=2)
overigFrame.pack_propagate(False)
"""einde grote frames"""

"""vormt en plaatst kleinere frames"""
orderlistFrame = Frame(orderFrame, width=screenWidth/3, height=screenHeight/3*2)
orderlistFrame.grid(column=0, row=0)
orderlistFrame.pack_propagate(False)

infoFrame = Frame(orderFrame, width=screenWidth/3, height=screenHeight/3)
infoFrame.grid(column=0, row=1)
infoFrame.grid_propagate(False)

#frame voor - aantal +
plusminFrame = Frame(overigFrame)
plusminFrame.pack()
#plusminFrame.grid_propagate(False)
"""einde kleinere frames"""

"""daadwerkelijke widgets"""



#scrollbar
scrollBar = Scrollbar(orderlistFrame)
scrollBar.pack(side=RIGHT, fill=Y)
#einde scrollbar
bedragTxtLabel = Label(infoFrame, text="Bedrag: ", bd=20)
bedragTxtLabel.grid(column=0, row=0)
bedragLabel = Label(infoFrame, textvariable=root.buying_list.total_str, bd=20)
bedragLabel.grid(column=1, row=0)
statusLabel = Label(infoFrame, text="Wachtend", bd=20)
statusLabel.grid(column=0, row=1)


#slider
aantalLabel = Label(plusminFrame, text=currentAantal, font="Arial 20")
aantalLabel.grid(column=1, row=0)

plusLabel = Label(plusminFrame, text=" + ", font="Arial 30")
plusLabel.grid(column=2, row=0)
minLabel = Label(plusminFrame, text=" − ", font="Arial 30")
minLabel.grid(column=0, row=0)

slider = Scale(overigFrame, orient=HORIZONTAL, showvalue=0, length=400)
#slider.grid(column=0, row=1)
slider.pack()



"""einde daadwerkelijke widgets"""
"""
bottomBar = Frame(root, width=SCREENWIDTH, height=40, bg="black")
bottomBar.grid(column=0, row=2, columnspan=3)
status = Label(bottomBar, text="Waiting for action", bd=1, relief=SUNKEN).pack(fill=Y)
"""
root.mainloop()