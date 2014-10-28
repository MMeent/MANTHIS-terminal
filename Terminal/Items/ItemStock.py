__author__ = 'Matthias'

from tkinter import *


class ItemStock:
    def __init__(self, item, amount: int):
        self.item = item
        self.amount = amount
        self.amountvar = StringVar()
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
        tile_bg = "#2B2B2B"
        tile_line = "#A3A3A3"
        tile_fontcollor = "#9ca9b6"

        tile = Frame(parent, bg=tile_bg, width=341, height=60)
        tile.grid_propagate(False)

        tile.testFrame = Frame(tile, width=170, bg=tile_line)
        tile.testFrame.grid(column=0, row=0)

        tile.test2Frame = Frame(tile, width=151, bg=tile_line)
        tile.test2Frame.grid(column=1, row=0)

        tile.name_label = Label(tile, text=self.item.get_name(), bg=tile_bg, font="Ariel 14 bold", fg=tile_fontcollor)
        tile.name_label.grid(column=0, row=1, sticky=W)

        tile.amount_label = Label(tile, text="Aantal: "+str(self.amount), bg=tile_bg, font=("Ariel", 12), fg=tile_fontcollor)
        tile.amount_label.grid(column=1, row=1, sticky=E)
        tile.price_label = Label(tile, text="Prijs: € "+str(self.get_price())+"0", bg=tile_bg, font="Ariel 10 bold", fg=tile_fontcollor)
        tile.price_label.grid(column=1, row=2, sticky=E)
        tile.item_stock = self

        def update():
            tile.price_label["text"] = "Prijs: € "+str(tile.item_stock.get_price())+"0"
            tile.amount_label["text"] = "Aantal: "+ str(tile.item_stock.get_amount())

        tile.update = update

        def on_click(event):
            tile.focus_set()
            tile.winfo_toplevel().buying_list.set_active_tile(tile)

        tile.on_click = on_click

        tile.bind("<Button-1>", on_click)

        self.tile = tile

        return tile