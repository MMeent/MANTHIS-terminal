__author__ = 'Matthias'

from tkinter import *


class ItemStock:
    def __init__(self, item, amount: int):
        self.item = item
        self.amount = amount
        self.tile = None

    def add(self, amount: int):
        self.amount += amount

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def get_name(self):
        return self.item.get_name()

    def get_price(self):
        return self.item.get_price() * self.amount

    def get_item(self):
        return self.item

    def get_tile(self):
        return self.tile

    def create_item_tile(self, parent):
        tile = Frame(parent, bg="gray", width=341, height=80)
        tile.grid_propagate(False)
        tile.name_label = Label(tile, text=self.item.get_name(), font=("Ariel", 14, "bold"))
        tile.name_label.grid(column=0, row=0)
        tile.amount_label = Label(tile, text=self.amount, font=("Ariel", 12))
        tile.amount_label.grid(column=1, row=0)
        tile.price_label = Label(tile, text=self.get_price(), font=("Ariel", 15, "bold"))
        tile.price_label.grid(column=2, row=0)
        tile.item_stock = self

        def update():
            tile.price_label["text"] = tile.item_stock.get_price()
            tile.amount_label["text"] = tile.item_stock.get_amount()

        tile.update = update

        def on_click(event):
            tile.focus_set()
            tile.master.buying_list.set_active_tile(tile)

        tile.on_click = on_click

        tile.bind("<Button-1>", on_click)

        self.tile = tile

        return tile