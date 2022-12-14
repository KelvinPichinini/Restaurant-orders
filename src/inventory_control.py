class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = dict(self.MINIMUM_INVENTORY)
        self.available = {'hamburguer', 'pizza', 'misto-quente', 'coxinha'}
        self.orders = []

    def add_new_order(self, customer, order, day):
        available_dishes = self.get_available_dishes()
        if order not in available_dishes:
            return False
        order_ingredients = self.INGREDIENTS[order]
        complete_order = (customer, order, day)
        for ingredient in order_ingredients:
            self.inventory[ingredient] -= 1
        self.orders.append(complete_order)

    def get_quantities_to_buy(self):
        wish_list = {}
        inv = self.inventory
        min_inv = self.MINIMUM_INVENTORY
        for item in inv:
            if inv[item] < min_inv[item]:
                wish_list[item] = min_inv[item] - inv[item]
            else:
                wish_list[item] = 0
        return wish_list

    def get_available_dishes(self):
        for dish in self.INGREDIENTS:
            for ingredient in self.INGREDIENTS[dish]:
                if self.inventory[ingredient] < 1:
                    self.available.discard(dish)
        return self.available
