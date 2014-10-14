__author__ = 'Matthias'

from Terminal.Items.Item import Item


class ItemStock:
    def __init__(self, item: Item, amount: int):
        self.item = item
        self.amount = amount

    def sell(self, amount: int):
        self.amount -= amount

    def add(self, amount: int):
        self.amount += amount

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def get_name(self):
        return self.item.get_name()

    def get_price(self):
        return self.item.get_price()

    def get_item(self):
        return self.item