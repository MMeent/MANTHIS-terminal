__author__ = 'Matthias'

from Terminal.Items.ItemStock import ItemStock
from tkinter import *


class BuyingList:
    def __init__(self):
        self.items = []
        self.total = self.get_total
        self.active_tile = None

    def add(self, stock: ItemStock):
        if (self.items[len(self.items) - 1]).get_name() == stock.get_name():
            (self.items[len(self.items) - 1]).add(1)
        else:
            self.items.append(stock)
        self.render()

    def render(self):
        pass

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def set_active_tile(self, tile: Frame):
        self.active_tile = tile