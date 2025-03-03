
class Favourite:
    def __init__(self, customer):
        self.customer = customer
        self.favourite_items = []

    def add_favourite(self, product):
            self.favourite_items.append(product)
            print(f"{product}hes been added to your favourites.")

    def view_favourite(self):
        """
        Display the customer's favourite products.

        :return: A list of favourite products or a message indicating no favourites exist.
        """
        
        if not self.favourite_items :
            return "Your Favourite Products: Your favourite is empty."
        return "Your Favourite Products:\n" + "\n".join(self.favourite_items )