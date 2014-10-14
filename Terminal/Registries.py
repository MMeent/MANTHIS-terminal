__author__ = 'Matthias'


class ItemRegistry:
    def __init__(self):
        self.items = Registry()

    def add(self, item):
        if not self.items[item.name]:
            self.items[item.name] = item

    def get(self, name):
        if not self.items[name]:
            return None
        return self.items[name]

    def get_items(self):
        return self.items.items()


class Registry(dict):
    def __missing__(self, key):
        return False