__author__ = 'Matthias'

from Terminal.Items.ItemStock import ItemStock
from tkinter import *


class Item:
    def __init__(self, name: str, price: float, image_link: str=None):
        print("n:" + name + "p:" + str(price))
        self.name = name
        self.price = price
        self.image_link = image_link
        self.tile = None

    def set_image(self, link: str):
        self.image_link = link

    def set_price(self, price: float):
        print(price)
        self.price = price

    def set_name(self, name: str):
        self.name = name

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_image_link(self):
        return self.image_link

    def get_item_stock(self, amount: int):
        return ItemStock(self, amount)

    def get_item_tile(self):
        return self.tile

    def create_item_tile(self, column=0, row=0, parent=None):
        tile_bg = "#2B2B2B"
        tile_line = "#A3A3A3"
        tile_fontcollor = "#9ca9b6"

        labelbg = "grey"
        tileheigth = 150
        tilewidth = 165
        tile = Frame(parent, bg=tile_bg, width=tilewidth, height=tileheigth, border=1)
        tile.grid_propagate(False)
        tile.grid(column=column, row=row)

        if self.image_link:
            img = PhotoImage(file=self.image_link)
            tile.img_lbl = Label(tile, image=img, height=100, width=tilewidth)
            tile.img_lbl.img = img
            tile.img_lbl.grid(column=0, row=0, columnspan=3)
        else:
            tile.img_lbl = Frame(tile, height=100, width=tilewidth)
            tile.img_lbl.grid(column=0, row=0, columnspan=3)

        tile.name_label = Label(tile, text=self.name, font="Arial 13 bold", bg=tile_bg, fg=tile_fontcollor)
        tile.name_label.grid(column=0, row=1, columnspan=3, sticky=W)

        #tile.prijs = Label(tile, text="Prijs:", font="Arial 11", bg=labelbg)
        #tile.prijs.grid(column=1, row=2, sticky=E)

        tile.price_label = Label(tile, text="Prijs: € "+str(self.price)+"0 ", font="Arial 11", bg=tile_bg, fg=tile_fontcollor)
        tile.price_label.grid(column=2, row=2, sticky=E)

        tile.item = self

        def on_click(event):
            print("click" + str(tile))
            tile.focus_set()
            tile.winfo_toplevel().buying_list.add(tile.item.get_item_stock(1))

        tile.on_click = on_click
        tile.bind("<Button>", tile.on_click)
        for child in tile.children.values():
            child.bind("<Button>", tile.on_click)
        self.tile = tile
        print(str(tile) + "  " + str(column) + "  " + str(row))
        return tile