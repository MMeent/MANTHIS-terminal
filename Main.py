from Terminal.BuyingList import BuyingList
from Terminal.Items.Item import Item
from Terminal.Registries import ItemRegistry

from tkinter import *

import json



root = Tk(screenName="Name", baseName="Name", className="Name")
root.item_registry = ItemRegistry()
root.resizable(width=FALSE, height=FALSE)
screenWidth = 1024
screenHeight = 720
root.geometry('{}x{}'.format(screenWidth, screenHeight))
buttonSize = 300
currentAantal = 26

"""functies voor slider en label"""


def plus_click(event):
    slider.set(slider.get() + 1)
    root.update()


def min_click(event):
    slider.set(slider.get() - 1)
    root.update()


def u(e):
    root.update()


def update():
    root.buying_list.active_tile_handler.get().item_stock.set_amount(slider.get())
    aantalLabel["text"] = root.buying_list.active_tile_handler.get().item_stock.get_amount()
    bedragLabel["text"] = root.buying_list.get_total()
    root.buying_list.active_tile_handler.active_tile.update()


def afrekenClick():
    return


"""einde functies"""


""" vormt en plaatst de drie grote frames die scherm opdelen"""
#oderFrame komt alles in wat met de info van de bestelling te maken heeft
orderFrame = Frame(root, width=(screenWidth / 3), height=screenHeight, bg="red")
orderFrame.grid(column=0, row=0, rowspan=2)
orderFrame.grid_propagate(False)
root.order_frame = orderFrame

#komen alle items in te staan (de artikelen)
itemFrame = Frame(root, width=(screenWidth / 3 * 2), height=(screenHeight - 100), bg="green")
itemFrame.grid(column=1, row=0, columnspan=2)
itemFrame.grid_propagate(False)
#overigFrame komt alle andere functionaliteiten in
overigFrame = Frame(root, width=(screenWidth / 3 * 2), height=100)
overigFrame.grid(column=1, row=1, columnspan=2)
overigFrame.pack_propagate(False)
"""einde grote frames"""


"""vormt en plaatst kleinere frames"""
orderlist = Frame(orderFrame, width=screenWidth/3, height=screenHeight/3*2)
orderlist.grid(column=0, row=0)
orderlist.pack_propagate(False)

infoFrame = Frame(orderFrame, width=screenWidth/3, height=screenHeight/3)
infoFrame.grid(column=0, row=1)
infoFrame.grid_propagate(False)

afrekenbuttonFrame = Frame(overigFrame, width=100, height=100)
afrekenbuttonFrame.pack(side=RIGHT, anchor=N)
afrekenbuttonFrame.pack_propagate(False)

#frame voor - aantal +
plusminFrame = Frame(overigFrame)
plusminFrame.pack(anchor=N)
#plusminFrame.grid_propagate(False)


"""einde kleinere frames"""


"""daadwerkelijke widgets"""
def onconfigure(e):
    ol_canvas.configure(scrollregion=ol_canvas.bbox("all"))

ol_canvas = Canvas(orderlist, width=screenWidth/3, height=screenHeight/3*2)

#scrollbar
scrollBar = Scrollbar(orderlist, command=ol_canvas.yview)
scrollBar.pack(side=RIGHT, fill=Y)

ol_canvas.configure(yscrollcommand=scrollBar.set)
ol_canvas.pack(expand=True)

orderlistFrame = Frame(ol_canvas)
orderlistFrame.pack()
root.orderlistFrame = orderlistFrame
ol_canvas.create_window((4, 4), window=orderlistFrame, anchor=NW)
orderlistFrame.bind("<Configure>", onconfigure)


root.buying_list = BuyingList(orderlistFrame)

#einde scrollbar
bedragTxtLabel = Label(infoFrame, text="Bedrag: ", bd=20)
bedragTxtLabel.grid(column=0, row=0)
bedragLabel = Label(infoFrame, textvariable=root.buying_list.total_str, bd=20)
bedragLabel.grid(column=1, row=0)
statusLabel = Label(infoFrame, text="Wachtend", bd=20)
statusLabel.grid(column=0, row=1)

root.scrollBar = scrollBar

#slider

aantalLabel = Label(plusminFrame, text=currentAantal, font="Arial 35",  width=2)
aantalLabel.grid(column=1, row=0)
root.update = update

plusLabel = Label(plusminFrame, text=" + ", font="Arial 46")
plusLabel.grid(column=2, row=0)
minLabel = Label(plusminFrame, text=" − ", font="Arial 46")
minLabel.grid(column=0, row=0)

plusLabel.on_click = plus_click
plusLabel.bind("<Button>", plusLabel.on_click)
minLabel.on_click = min_click
minLabel.bind("<Button>", minLabel.on_click)

slider = Scale(overigFrame, orient=HORIZONTAL, showvalue=0, from_=1, to=25, command=u)
slider.pack(fill=X, side=BOTTOM)
root.slider = slider

afrekenButton = Button(afrekenbuttonFrame, text="Afrekenen", command=afrekenClick, height=50)
afrekenButton.pack(fill=BOTH)


with open("Terminal/Items/Items.json") as jsonfile:
    data = json.load(jsonfile)
    for item in data:
        root.item_registry.add(Item(item["name"], item["price"]))

i = 0
for item in root.item_registry.get_items():
    print(item[1].tile)
    item[1].create_item_tile(i % 4, i // 4, itemFrame)
    i += 1

itemFrame.grid()

"""einde daadwerkelijke widgets"""

root.mainloop()