from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from products import ProductManager
from customer import Customer   
from cart import ShoppingCart
from membership import Membership
from favorite import Favourite


console = Console()  

def display_menu():  
    menu = Table(title="[bold magenta] Areej Beauty Store - Main Menu[/bold magenta]")  
    menu.add_column("Option", justify="center", style="cyan", no_wrap=True) 
    menu.add_column("Description", style="white")  

    # Add options to the menu
    menu.add_row("1", "View Makeup Products")
    menu.add_row("2", "View Skincare Products")
    menu.add_row("3", "View All Products")
    menu.add_row("4", "Search for a Product")
    menu.add_row("5", "View Recommendations")
    menu.add_row("6", "Add a Product to the Cart")
    menu.add_row("7", "View Shopping Cart")
    menu.add_row("8", "Remove a Product from the Cart")
    menu.add_row("9", "Checkout")
    menu.add_row("10", "View Membership Information")
    menu.add_row("11", " Add a prodect to My Favorites")
    menu.add_row("12", "View My Favorites")
    menu.add_row("13", "Exit")

    console.print(menu)  

def main():
    # User login function or account creation
    user = Customer.authentication()
    if not user:
        return 
    user_membership = Membership(user.membership)  

    
    product_manager = ProductManager()  
    shopping_cart = ShoppingCart(user)  
    favourite = Favourite(user)

    # Adding some products
    product_manager.add_product("Lipstick", 150, 20, "Makeup")  
    product_manager.add_product("Foundation", 100, 15, "Makeup")
    product_manager.add_product("Concealer", 200.0, 10, "Makeup")
    product_manager.add_product("Eyeshadow", 360, 25, "Makeup")
    product_manager.add_product("Mascara", 123, 30, "Makeup")
    product_manager.add_product("Face Cream", 116, 12, "Skincare")  
    product_manager.add_product("Sunscreen", 99, 18, "Skincare") 

    console.print(Panel.fit(f"  Welcome [bold magenta]{user.name}[/bold magenta] to Areej Beauty Store!\n"
                            f"Your membership: [bold cyan]{user.membership}[/bold cyan]", 
                            title="[bold yellow]Areej Beauty[/bold yellow]", style="blue"))
    search_term =None
    while True:
        display_menu()  
        choice = console.input("\n[bold yellow] Enter the option number: [/bold yellow] ")
        
        if choice == "1":
            console.print("\n[bold magenta] Makeup Products:[/bold magenta]\n")
            console.print(product_manager.list_product(category="Makeup"))


        elif choice == "2":
            console.print("\n[bold green] Skincare Products:[/bold green]\n")
            console.print(product_manager.list_product(category="Skincare"))
        
        elif choice == "3":
            console.print("\n[bold blue] All Products:[/bold blue]\n")
            console.print(product_manager.list_product())
        
        elif choice == "4":
            search_term = console.input("\n[bold] Enter the product name to search for:[/bold] ")
            results = product_manager.search_product(search_term)

            console.print(f"\n[bold cyan] Search Results for '{search_term}':[/bold cyan]\n")
            if results:
                console.print(results)
            else:
                console.print("[bold red] No products found.[/bold red]")

        
        elif choice == "5":
            if search_term:
                console.print("\n[bold yellow] Recommended Products for You:[/bold yellow]\n")
                recommendations = product_manager.recommend_products(search_term)
                if recommendations:
                   for recommendation in recommendations:
                       console.print(recommendation)
                else:
                    console.print("[bold red]No recommendations found based on your last search.[/bold red]")
            else:
                console.print("[bold red]No search history found. Please search for a product first.[/bold red]")

        
        elif choice == "6":
            product_name = console.input("\n🛒 [bold] Enter the product name to add to the cart:[/bold] ")
            product = product_manager.get_product(product_name)
            if product:
                shopping_cart.add_cart(product)
            else:
                console.print("[bold red]Product not found.[/bold red]")

        # View shopping cart
        elif choice == "7":
            shopping_cart.view_cart()

        # Remove a product
        elif choice == "8":
            product_name_to_remove = console.input("\n[bold] Enter the name of the product you want to remove:[/bold] ")
            shopping_cart.remove_cart(product_name_to_remove)


        elif choice == "9":
            shopping_cart.checkout()

        # membership information 
        elif choice == "10":
            console.print(Panel.fit(str(user_membership), title="[bold yellow]Membership Info [/bold yellow]", style="cyan"))

        elif choice == "11":
            product_name_to_favourite = console.input("\n[bold] Enter the product name to add to your favourites:[/bold] ")
            product = product_manager.get_product(product_name_to_favourite)
            if product:
                favourite.add_favourite(product_name_to_favourite)
            else:
                console.print("[bold red]Product not found.[/bold red]")
                
        elif choice == "12":
            console.print("\n[bold blue] Your Favourite Products:[/bold blue]\n")
            console.print(favourite.view_favourite())    
            
    
        elif choice == "13":
            console.print("\n[bold green] Thank you for visiting Areej Beauty! See you soon.[/bold green] ")
            break

        
        else:
            console.print("[bold red]Invalid choice, please try again.[/bold red]")

if __name__ == "__main__":
    main()  