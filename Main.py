from Terminal.BuyingList import BuyingList
from Terminal.Items.Item import Item
from Terminal.Registries import ItemRegistry

import pymfrc
import connection

from tkinter import *

import random
import json

connect = connection.serverConnection()
rnd = random.randrange

root = Tk(screenName="Name", baseName="Name", className="Name")
root.item_registry = ItemRegistry()
root.resizable(width=FALSE, height=FALSE)
screenWidth = 1024
screenHeight = 720
root.geometry('{}x{}'.format(screenWidth, screenHeight))
buttonSize = 300
currentAantal = 26
bg2 = "#3c3f41"
bg = "#2B2B2B"
fontcollor = "#9ca9b6"


bgOverigFrame = "#3c3f41"

"""functies voor slider en label"""


def plus_click(event):
    slider.set(slider.get() + 1)
    root.update()


def min_click(event):
    slider.set(slider.get() - 1)
    root.update()


def delete_click(event):
    root.buying_list.active_tile_handler.get().delete()
    root.update()


def u(e):
    root.update()


def update():
    root.buying_list.active_tile_handler.get().item_stock.set_amount(slider.get())
    aantalLabel["text"] = root.buying_list.active_tile_handler.get().item_stock.get_amount()
    bedragLabel["text"] = root.buying_list.get_total()
    root.buying_list.active_tile_handler.active_tile.update()


def afrekenClick():
    total = root.buying_list.get_total()
    scan = pymfrc.scan(2)
    id = str(scan[:4])
    seed = str(scan[-12:])
    new_seed = ""
    for value in range(0, 11):
        new_seed += str(rnd(0, 9))


    print("id " + id)
    print("hash " + seed)
    print("new hash: " + new_seed)

    while not id + new_seed == pymfrc.write(2, id + new_seed):
        pass
    if not connect.transact(id, new_seed, total, seed):
        pass
    root.buying_list.clear()



"""einde functies"""


""" vormt en plaatst de drie grote frames die scherm opdelen"""
#oderFrame komt alles in wat met de info van de bestelling te maken heeft
orderFrame = Frame(root, width=(screenWidth / 3), height=screenHeight, bg=bg2)
orderFrame.grid(column=0, row=0, rowspan=2)
orderFrame.grid_propagate(False)
root.order_frame = orderFrame

#komen alle items in te staan (de artikelen)
itemFrame = Frame(root, width=(screenWidth / 3 * 2), height=(screenHeight - 100), bg="green")
itemFrame.grid(column=1, row=0, columnspan=2)
itemFrame.grid_propagate(False)
#overigFrame komt alle andere functionaliteiten in
overigFrame = Frame(root, width=(screenWidth / 3 * 2), height=100, bg=bgOverigFrame)
overigFrame.grid(column=1, row=1, columnspan=2, sticky=S)
overigFrame.pack_propagate(False)
"""einde grote frames"""


"""vormt en plaatst kleinere frames"""
orderlist = Frame(orderFrame, width=screenWidth/3, height=screenHeight/3*2, bg=bg)
orderlist.grid(column=0, row=0)
orderlist.pack_propagate(False)

infoFrame = Frame(orderFrame, width=screenWidth/3, height=screenHeight/3, bg=bg2)
infoFrame.grid(column=0, row=1)
infoFrame.grid_propagate(False)

afrekenbuttonFrame = Frame(overigFrame, width=100, height=100)
afrekenbuttonFrame.pack(side=RIGHT, anchor=N)
afrekenbuttonFrame.pack_propagate(False)

#frame voor - aantal +
plusminFrame = Frame(overigFrame, bg=bgOverigFrame)
plusminFrame.pack(anchor=N)
#plusminFrame.grid_propagate(False)


"""einde kleinere frames"""


"""daadwerkelijke widgets"""


def ol_onconfigure(e):
    ol_canvas.configure(scrollregion=ol_canvas.bbox("all"))


def i_onconfigure(e):
    i_canvas.configure(scrollregion=i_canvas.bbox("all"))

ol_canvas = Canvas(orderlist, width=screenWidth/3-20, height=screenHeight/3*2, bg=bg2)

#scrollbar
scrollBar = Scrollbar(orderlist, command=ol_canvas.yview)
scrollBar.pack(side=RIGHT, fill=Y)

ol_canvas.configure(yscrollcommand=scrollBar.set)
ol_canvas.pack(expand=True)

orderlistFrame = Frame(ol_canvas)
orderlistFrame.pack()
root.orderlistFrame = orderlistFrame
ol_canvas.create_window((4, 4), window=orderlistFrame, anchor=NW)
orderlistFrame.bind("<Configure>", ol_onconfigure)

root.buying_list = BuyingList(orderlistFrame)
# einde scrollbar
# scrollbar voor tile frame
i_canvas = Canvas(itemFrame, width=screenWidth/3*2-24, height=screenHeight-100, bg=bg)

itemScrollbar = Scrollbar(itemFrame, command=i_canvas.yview)
itemScrollbar.pack(side=RIGHT, fill=Y)

i_canvas.configure(yscrollcommand=itemScrollbar.set)
i_canvas.pack(expand=True)

items = Frame(i_canvas)
items.pack()
root.itemFrame = items
i_canvas.create_window((4, 4), window=items, anchor=NW)
items.bind("<Configure>", i_onconfigure)

bedragtxtFrame = Frame(infoFrame, bg=bg2)
bedragtxtFrame.pack(pady=20)

bedragTxtLabel = Label(bedragtxtFrame, text="Eindprijs: €", fg=fontcollor, font="Arial 25 bold", bg=bg2)
bedragTxtLabel.grid(column=0, row=0)
bedragLabel = Label(bedragtxtFrame, textvariable=root.buying_list.total_str, fg=fontcollor, font="Arial 25 bold", bd=0, bg=bg2)
bedragLabel.grid(column=1, row=0)
nullLabel = Label(bedragtxtFrame, text="0", fg=fontcollor, font="Arial 25 bold", bd=0, bg=bg2)
nullLabel.grid(column=2, row=0)
statusLabel = Label(infoFrame, text="Wachtend", bd=20, fg=fontcollor, bg=bg2)
statusLabel.pack(anchor=S)

root.scrollBar = scrollBar

#slider

aantalLabel = Label(plusminFrame, text=currentAantal, font="Arial 35",  width=2, bg=bgOverigFrame, fg=fontcollor)
aantalLabel.grid(column=2, row=0)
root.update = update

deleteLabel = Label(plusminFrame, text=" × ", font="Arial 46", bg=bgOverigFrame, fg=fontcollor)
deleteLabel.grid(column=0, row=0)
plusLabel = Label(plusminFrame, text=" + ", font="Arial 46", bg=bgOverigFrame, fg=fontcollor)
plusLabel.grid(column=3, row=0)
minLabel = Label(plusminFrame, text=" − ", font="Arial 46", bg=bgOverigFrame, fg=fontcollor)
minLabel.grid(column=1, row=0)

deleteLabel.on_click = delete_click
deleteLabel.bind("<Button>", deleteLabel.on_click)
plusLabel.on_click = plus_click
plusLabel.bind("<Button>", plusLabel.on_click)
minLabel.on_click = min_click
minLabel.bind("<Button>", minLabel.on_click)

slider = Scale(overigFrame, orient=HORIZONTAL, showvalue=0, from_=1, to=25, command=u, bg=fontcollor, troughcolor=fontcollor)
slider.pack(fill=X, side=BOTTOM)
root.slider = slider

afrekenButton = Button(afrekenbuttonFrame, text="Afrekenen", command=afrekenClick, height=50, bg=bg2, relief=GROOVE, font="Arial 12 bold", fg=fontcollor)
afrekenButton.pack(fill=BOTH)


with open("Terminal/Items/Items.json") as jsonfile:
    data = json.load(jsonfile)
    for item in data:
        try:
            root.item_registry.add(Item(item["name"], item["price"], item["url"]))
        except Exception:
            root.item_registry.add(Item(item["name"], item["price"]))
i = 0
for item in root.item_registry.get_items():
    print(item[1].tile)
    item[1].create_item_tile(i % 4, i // 4, items)
    i += 1

itemFrame.grid()

"""einde daadwerkelijke widgets"""

root.mainloop()