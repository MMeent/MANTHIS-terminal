__author__ = 'Matthias'


class ItemRegistry:
    def __init__(self):
        self._items = Registry()

    def add(self, item):
        if not self._items[item.name]:
            self._items[item.name] = item

    def get(self, name):
        return self._items[name]

    def get_items(self):
        return self._items.items()


class Registry(dict):
    def __missing__(self, key):
        return None