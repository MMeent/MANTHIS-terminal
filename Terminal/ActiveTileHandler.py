__author__ = 'Matthias'

from tkinter import *
from Terminal.Items.ItemStock import ItemStock
from Terminal.Items.Item import Item


class ActiveTileHandler:
    def __init__(self):
        self.active_tile = ItemStock(Item("", 0), 1).create_item_tile(None)

    def set_tile(self, tile: Frame):
        self.active_tile = tile

    def set(self, amount: int):
        self.active_tile.item_stock.set(amount)
        self.active_tile.master.buying_list.render()

    def get(self):
        return self.active_tile

    def add(self, amount: int):
        self.active_tile.item_stock.add(amount)