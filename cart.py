# Cart will contain customer from customer id and item
# Cart have function to operate cashier
class Cart:
    def __init__(self, customer):

        self.customer = customer
        self.items = {}

    def add_item(self, item):

        self.items[item.name] = item

    def update_item(self, item_name, new_name, new_quantity, new_price):

        if item_name in self.items:
            item = self.items[item_name]
            item.name = new_name
            item.quantity = new_quantity
            item.price = new_price

            self.items[new_name] = self.items.pop(item_name)

            print("Keranjang berhasil diubah")
        else:
            print("Item tidak ada di dalam keranjang")

    def check_order(self):
        if not self.items :
          print("Keranjang kosong! Masukan item untuk belanja")

        else:

          print(f"List belanja {self.customer.customer_id}:")
          for item_name, item in self.items.items():
            print(f"{item_name} - Quantity: {item.quantity} - Price: {item.price}")

    def calculate_total (self):

        total = 0
        for item in self.items.values():
          total += item.price * item.quantity
        return total

    def calculate_discount (self):

        total = self.calculate_total()
        if total >= 500_000:
          discount = total * 0.10
        elif total >= 300_000:
          discount = total * 0.08
        elif total >= 200_000:
          discount = total * 0.05
        else :
          discount = 0
        return discount

    def total_after_discount (self):

        total = self.calculate_total()
        discount = self.calculate_discount()
        total_after_discount = total - discount
        return total_after_discount

    def delete_item (self, item_name):

        if item_name in self.items :
          del self.items[item_name]
          print ("Item berhasil dihapus")
        else :
          print ("Item tidak ada di dalam keranjang")

    def reset_transaction (self):

        self.items = {}
        print ("Keranjang sudah kosong")

    def print_invoice (self):

        print("=========== INVOICE ===========")
        print(f"Customer ID: {self.customer.customer_id}")
        print("Items:")
        for item_name, item in self.items.items():
          print(f"{item_name} - Quantity: {item.quantity} - Price: {item.price}")
        print("===")
        print(f"Total: {self.calculate_total()}")
        print(f"Discount: {self.calculate_discount()}")
        print(f"Total Setelah Discount: {self.total_after_discount()}")
        print("======================")