__author__ = 'Matthias'

from Terminal.Items.ItemStock import ItemStock


class Item:
    def __init__(self, name: str, price: float, image_link: str=None):
        self.name = name
        self.price = price
        self.image_link = image_link

    def set_image(self, link: str):
        self.image = link

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

    def get_item_stack(self, amount: int):
        return ItemStock(self, amount)