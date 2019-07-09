import os
from exceptions import ItemHasNoPriceError

class Checkout:

    class Discount:
        def __init__(self, quantity, price):
            self.quantity = quantity
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def get_prices(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(
                "The file {} does not exist".format(filename)
            )
        with open(filename, "r") as infile:
            for line in infile:
                tokens = line.split()
                self.add_item_price(tokens[0], int(tokens[1]))

    def add_item(self, item):
        if item not in self.prices:
            raise ItemHasNoPriceError("Item {} has no price".format(item))
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)

        return total

    def add_discount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.quantity:
                total += self.calculate_item_discounted_total(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

    def calculate_item_discounted_total(self, item, cnt, discount):
        total = 0
        num_of_discounts = cnt/discount.quantity
        total += num_of_discounts * discount.price
        remaining = cnt % discount.quantity
        total += remaining * self.prices[item]

        return total
