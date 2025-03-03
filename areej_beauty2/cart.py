class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.cart_item = {} #Store products such as price and quantity
        

        #Add a product to the cart
    def add_cart(self, product, quantity=1):
        if product.stock < quantity:
            print(f"Quantity required is not available, Quantity available: {product.stock}")
            return
        if product.name in self.cart_item:
            self.cart_item[product.name][1] += quantity   #Determines the quantity
        else:
            self.cart_item[product.name] = [product.price, quantity]
            product.stock -= quantity #Reduces inventory after adding it
            print(f"Added {quantity} from {product.name} To the shopping cart.")
        
       # Delete the product from the shopping cart using the name
    def remove_cart(self, product_name):
        remove_item = self.cart_item.pop(product_name, None)
        if remove_item:
            print(f" {product_name} has been removed From the cart.")
        else:
            print("the product is not available in the cart.")

            
       #View cart content
    def view_cart(self):
        if not self.cart_item:
            print("Your shopping cart is empty! Add some products to the cart to complete your order")
            return
        print("\n Shopping cart contents:")
        total = 0
        for product, details in self.cart_item.items():
            price, quantity = details
            total += price * quantity
            print(f"- {product}: {quantity} * {price} riyal$ = {quantity * price} riyal$")
            print(f"\n total: {total} riyal$")
       # Function for payment process
    def checkout(self):
        if not self.cart_item:
            print("you connot complete the payment")   
            return
        self.view_cart()
        delivery_address  =input("\n Please enter your delivery address: ")
        if not delivery_address:
            print("Address is required.")
            return
        
        print("\n Your purchase was completed successfully. Thank you for choosing Areej Beauty")
        print(f"Delivery address: {delivery_address}")
        print("the invoice:")
        for product, details in self.cart_item.items():
            price, quantity = details
            print(f"-{product}: {quantity * price} riyal$ = {quantity * price} riyal$")
        self.cart_item.clear()    #   The cart will be empty after purchase
        



