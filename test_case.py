# Note : This test case should run separately

# Create a Customer object
dianda = Customer("dianda")

# Create a Cart object for the customer 'dianda'
dianda.cart = Cart(dianda)

# Create an Item object named "item"
item = Item("daging", 1, 180000)

# Add the "item" to the 'dianda' cart
dianda.cart.add_item(item)

# Create another Item object named "item2"
item2 = Item("beras", 1, 30000)

# Add the "item2" to the 'dianda' cart
dianda.cart.add_item(item2)

# Check the order for the 'dianda' cart
dianda.cart.check_order()

# update item in cart
dianda.cart.update_item("daging", "kacang ijo", 3, 30000)

# delete item in cart
dianda.cart.delete_item("beras")

# reset all item in cart
dianda.cart.reset_transaction()

# To count total in cart 
dianda.cart.calculate_total()

# To count if get discount
dianda.cart.calculate_discount()

# To count net total
dianda.cart.total_after_discount()

# To print Invoice
dianda.cart.print_invoice()
