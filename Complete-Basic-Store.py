class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    # Adding a __str__ method makes it easy to print the object beautifully
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} in stock)"
    
# 2. THE STORE CLASS
class Store:
    def __init__(self):
        self.products = [] # A list to hold our Product Objects
        
    def add_to_inventory(self, product):
        self.products.append(product)
        
    def display_inventory(self):
        print("\n--- Store Inventory ---")
        for p in self.products:
            print(p)
        print("--------------------")
        
    def find_product(self, name):
        # Look through inventory and return the object if the name matches
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None
    
# 3. THE SHOPPING CART CLASS
class ShoppingCart:
    def __init__(self):
        self.items = {} # Dictionary to hold {product_object: quantity}
        
    def add_product(self, product, quantity):
        # First, check how many of this item are already in the cart
        current_qty = self.items.get(product, 0)
        
        # Check if the store has enough stock for the total requested
        if product.stock >= (current_qty + quantity):
            self.items[product] = current_qty + quantity
            print(f"Added {quantity} * {product.name} to cart.")
        else: print(f"Sorry, not enough stock for {product.name}. Only {product.stock} available.")
        
    def remove_product(self, product, quantity):
        if product in self.items:
            # If trying to remove more than or exactly what's in the cart, remove the item entirely
            if self.items[product] <= quantity:
                del self.items[product]
                print(f"Removed all {product.name}s from cart.")
            else: 
                self.items[product] -= quantity
                print(f"Removed {quantity} * {product.name} from cart.")
        else:
            print(f"{product.name} is not in your cart.")
            
    def view_cart(self):
        print("\n--- Your Shopping Cart ---")
        if not self.items:
            print("Your cart is empty.")
        else:
            for product, quantity in self.items.items():
                print(f"{product.name}: {quantity} @ ${product.price:.2f} each")
        print("----------------------------")
        
    def get_total(self):
        # Calculate total by multiplying price by quantity for every item in the dictionary
        total = sum(product.price * quantity for product, quantity in self.items.items())
        return total

    def checkout(self):
        if not self.items:
            print("Cart is empty. Nothing to checkout.")
            return

        print("\n--- Checkout ---")
        for product, quantity in self.items.items():
            # Reduce the actual product's stock attribute
            product.stock -= quantity
            
        total = self.get_total()
        print(f"Total paid: ${total:.2f}")
        
        # Clear the cart after a successful checkout
        self.items.clear()  
        print("Checkout complete! Thank you for shopping.")
        
        
# 1. Setup the store and add 5 products
my_store = Store()
my_store.add_to_inventory(Product("Laptop", 999.99, 5))
my_store.add_to_inventory(Product("Mouse", 25.50, 20))
my_store.add_to_inventory(Product("Keyboard", 45.00, 15))
my_store.add_to_inventory(Product("Monitor", 150.00, 10))
my_store.add_to_inventory(Product("HDMI Cable", 15.00, 50))

# 2. Display what the store has
my_store.display_inventory()

# 3. Create a cart for a user
my_cart = ShoppingCart()

# 4. Find products and add them to the cart
laptop = my_store.find_product("laptop")
mouse = my_store.find_product("mouse")

my_cart.add_product(laptop, 1)
my_cart.add_product(mouse, 2)

# Try to add more laptops than the store has (will trigger stock warning)
my_cart.add_product(laptop, 6)

# 5. View cart and checkout
my_cart.view_cart()
my_cart.checkout()

# 6. Check store inventory again to prove stock decreased!
my_store.display_inventory()