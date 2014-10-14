__author__ = 'Matthias'

from Terminal.Items.ItemStock import ItemStock
from Terminal.ActiveTileHandler import ActiveTileHandler
from tkinter import *


class BuyingList:
    def __init__(self):
        self.total_str = StringVar()
        self.items = []
        self.total = self.get_total
        self.active_tile_handler = ActiveTileHandler()
        self.total()

    def add(self, stock: ItemStock):
        if self.active_tile_handler.get().get_name() == stock.get_name():
            self.active_tile_handler.add(1)
        else:
            self.items.append(stock)
        self.total()
        self.render()

    def render(self):
        pass

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        self.total_str.set(str(total))
        return total

    def set_active_tile(self, tile: Frame):
        self.active_tile_handler.set_tile(tile)