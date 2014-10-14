__author__ = 'Matthias'

from Terminal.Items.Item import Item
from tkinter import *


class ItemStock:
    def __init__(self, item: Item, amount: int):
        self.item = item
        self.amount = amount

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

    def create_item_tile(self, parent):
        tile = Frame(parent, bg="gray")
        tile.grid_propagate(False)
        name_label = Label(tile, text=self.item.get_name(), font=("Ariel", 14, "bold"))
        name_label.grid(column=0, row=0)
        amount_label = Label(tile, text=self.amount, font=("Ariel", 12))
        amount_label.grid(column=1, row=0)
        price_label = Label(tile, text=self.get_price(), font=("Ariel", 15, "bold"))
        price_label.grid(column=2, row=0)
        tile.item_stock = self

        def on_click(event):
            tile.focus_set()
            tile.master.buying_list.set_active_tile(tile)

        tile.on_click = on_click
        tile.bind("<Button-1>", on_click)

        return tile