class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name][1] += quantity
        else:
            self.items[item_name] = [price, quantity]
    
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Error: {} not found in the cart" .format(item_name))
    
    def total(self):
        total_price = sum(price * quantity for price, quantity in self.items.values())
        return total_price
    
    def display_cart(self):
        print("Items in the cart: ")
        for item, details in self.items.items():
            print(f"{item}: Price - Rs{details[0]}, Quantity - {details[1]}")

crt = ShoppingCart()

crt.add_item("Apple",20,2)
crt.add_item("Pineapple",40,1)
crt.add_item("Orange",30,2)

crt.display_cart()

total_price = crt.total()
print(f"Total Price : Rs{total_price}")

crt.remove_item("Pineapple")

crt.display_cart()

new_price = crt.total()
print(f"Total Price: Rs{new_price}")