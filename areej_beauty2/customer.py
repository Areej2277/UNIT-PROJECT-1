import json
import getpass
import os

class Customer:
    #Client database file
    Customer_db = 'customeer_db.json'    

    def __init__(self, name: str, contact: str, password: str, membership:str="White"):
        self.name = name  
        self.contact = contact 
        self.password = password 
        self.membership = membership  #memdership type
    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact}, Memdership: {self.membership}"
    
    @staticmethod
    def load_customers():
        """
Load clients from database in json format.
 :return: A dictionary containing clients if the file exists, or an empty dictionary.
"""
        if os.path.exists(Customer.Customer_db):
            with open(Customer.Customer_db, 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_customers(customers):
        with open(Customer.Customer_db, 'w') as file:
            json.dump(customers, file, indent=4)

    @staticmethod
    # A function to create a new account
    def register(): 
        print("\nCreate a new account at Areej Beauty")
        

        name = input("Please enter your name: ")
    
        while not name:
            print("The name cannot be empty!")
            name = input("Please Enter your name: ")

        
        contact = input("Please enter your email or phone number: ")
        while not contact:
            print("You must enter your email or phone number! ")
            contact = input("Please enter your email or phone number: ")
        customers = Customer.load_customers()
        if contact in customers:
            print("This account is already registered! ")
            return Customer.login()


        password = getpass.getpass("Enter the password: ")
        while not password:
            print("The password cannot be empty!")
            password = getpass.getpass("Enter the password: ")

        
        membership = input("Choose your membership  (White, Black, Gold): ").capitalize()
        if membership not in ["White", "Black", "Gold"]:
            print("Invalid membership! Defaulting to 'White'.")
            membership = "White"
                
        
        customer = Customer(name, contact, password, membership)
        customers[contact] = {
            'name': customer.name,
            'password': customer.password,
            'membership': customer.membership,
        }
        Customer.save_customers(customers)

        print(f"\nWelcome {customer.name}! You have successfully registered at Areej Beauty store.\n")
        print(f"Membership: {customer.membership}")
        return customer
        
    @staticmethod
    # login
    def login():
        print("\nLog in to Areej Beauty store")
        contact = input("Please enter your email or phone number: ")
        customers = Customer.load_customers()
        if contact not in customers:
            print("The account does not exist. Please create an account.")
            return Customer.register()
        
            #Hide the password
        password = getpass.getpass("Enter the password: ")
        if customers[contact]['password'] != password:
            print("The password is incorrect, Please try again.")
            return None
            
        customer_data = customers[contact]
        customer = Customer(customer_data['name'], contact, password, customer_data['membership'])
        print(f"\nWelcome {customer.name}! You have successfully logged in to Areej Beauty store.\n")
        return customer

    @staticmethod
    # logout
    def logout():
        print("\nYou have successfully logged out from Areej Beauty store.")
        return None

    @staticmethod
    #The user can choose to register or log in
    def authentication():
        print("\n Welcome to Areej Beauty store ")
        choice = input("Do you have an account? (Yes/No): ")
        if choice == "Yes":
            return Customer.login()
        else:
            return Customer.register()


