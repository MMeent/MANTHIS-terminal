__author__ = 'Matthias'

import Terminal.Items.ItemStock
from tkinter import *


class Item:
    def __init__(self, name: str, price: float, image_link: str=None):
        self.name = name
        self.price = price
        self.image_link = image_link
        self.tile = self.create_item_tile()

    def set_image(self, link: str):
        self.image_link = link

    def set_price(self, price: float):
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

    def create_item_tile(self, parent: Widget=None):
        tile = Frame(parent, bg="black")
        tile.grid_propagate(False)
        if self.image_link:
            img = PhotoImage(file=self.image_link)
            img_lbl = Label(tile, image=img, height=50, width=50)
            img_lbl.img = img
            img_lbl.grid(column=0, row=0, columnspan=3)
        else:
            img_lbl = Label(tile, height=50, width=50, color="gray")
            img_lbl.grid(column=0, row=0, columnspan=3)
        name_label = Label(tile, text=self.name, font=(Arial, 12))
        name_label.grid(column=0, row=1, columnspan=2)
        price_label = Label(tile, text=str(self.price), font=("Arial", 14, "bold"))
        price_label.grid(column=2, row=1)
        tile.item = self

        def on_click(event):
            tile.focus_set()
            tile.master().buying_list.add(tile.item.get_item_stock(1))

        tile.on_click = on_click
        tile.bind("<Button-1>", tile.on_click)
        return tile