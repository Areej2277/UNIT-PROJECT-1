
#Determine which category each product represents
class Prodect:  
    def __init__(self, name: str , price: float, stock: int, category: str):
        self.name = name     
        self.price = price   
        self.stock = stock  
        self.category = category  

    # function to represent the product in text form
    def __str__(self):
        if self.stock<= 0:
            return f"{self.name} - {self.category} - Out of stock"
        return f"{self.name} - {self.category} - ${self.price} - Quantity: {self.stock}"

# Define a category for product management
class ProductManager: 
    def __init__(self):

        self.products = []

    # Function to add a new product
    def add_product(self, name, price, stock, category):
        product = Prodect(name, price, stock, category)
        self.products.append(product)  

    # F to display all products
    def list_product(self, category=None):
        filtered_products = self.products if category is None else [p for p in self.products if p.category.lower() == category.lower()]
        if not filtered_products or all(product.stock <= 0 for product in filtered_products):
            return "Out of stock"
        return "\n".join([str(product) for product in filtered_products])

    # Function to search for a product by name
    def search_product(self, search_term):
        found_products = [str(product) for product in self.products if search_term.lower() in product.name.lower()]
        return "\n".join(found_products) if found_products else "No products found."
    
    #Funation to recommend products
    def recommend_products(self, search_item):
        if not search_item: 
            return ["Invalid search term. Please enter a valid product name."]
        search_item = search_item.lower()
        recommendations = [
            f"Try our best-selling {product.name} in the {product.category} category!"
            for product in self.products
            if search_item in product.name.lower() or search_item in product.category.lower()
        ]
        return recommendations if recommendations else ["No recommendation available for your search."]
#Funation to get product by name
    def get_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None
    
       #Inventory occurs after purchase
    def update_stock(self, product_name, quantity): 
        product = self.get_product(product_name)
        if product:
            if product.stock < quantity:
                print(f"Not enough stock for {product.name}. Available: {product.stock}")
                return
            product.stock -= quantity
            print(f"Quantity has been updated for {product.name}. The remaining quantity: {product.stock}")
        else:
            print(f"The product {product_name} is not found.")





            
    