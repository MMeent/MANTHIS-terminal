__author__ = 'Matthias'

from Terminal.Items.ItemStock import ItemStock
from Terminal.ActiveTileHandler import ActiveTileHandler
from tkinter import *


class BuyingList:
    def __init__(self, root):
        self.master = root
        self.total_str = StringVar()
        self.items = []
        self.total = self.get_total
        self.active_tile_handler = ActiveTileHandler()
        self.total()

    def add(self, item_stock: ItemStock):
        if self.active_tile_handler.get().item_stock.get_name() == item_stock.get_name():
            self.active_tile_handler.add(1)
        else:
            self.items.append(item_stock)

        #self.master.orderlistFrame
        self.total()
        self.render(item_stock)

    def render(self, item_stock: ItemStock):
        item_stock.create_item_tile(self.master).pack()

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        self.total_str.set(str(total))
        return total

    def set_active_tile(self, tile: Frame):
        self.active_tile_handler.set_tile(tile)