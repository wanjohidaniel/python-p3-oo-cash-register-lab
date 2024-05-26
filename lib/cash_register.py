#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            self.total = round(self.total)  # Assuming rounding to the nearest whole number
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0
