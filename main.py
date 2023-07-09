# Create an object for customer
class Customer:

    def __init__(self, customer_id):
        self.customer_id = customer_id


# Create an object for item
class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price