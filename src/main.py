import uuid
from datetime import datetime
import mysql.connector
from receipt.controller import Controller as ReceiptController
from products.controller import Controller as ProductController
from user.controller import Controller as UserController
import os

# connect to database
connection = mysql.connector.connect(
host="localhost",
user="admin",
password="root",
database="grocerystore"
)

if connection.is_connected():
     print("Connected to MySQL database")

def main():
    clear_screen()
    # main menu
    main_menu()

    connection.close()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    print("Welcome to the Grocery Store")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    while choice != 3:
        if choice == 1:
            clear_screen()
            usrname = input("Enter your username: ")
            password = input("Enter your password: ")
            controller = UserController()
            lgn_succ, type = controller.login(connection, usrname, password)
            if lgn_succ:
                clear_screen()
                print("Login successful")
                logged_menu(type)
            else:
                clear_screen()
                print("Invalid username or password")


        elif choice == 2:
            clear_screen()
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")
            name = input("Enter your name: ")
            phonenumber = input("Enter your phone number: ")
            while check_empty(username) or check_empty(password) or check_empty(email) or check_empty(name) or check_empty(phonenumber):
                clear_screen()
                print("You cannot leave any fields empty")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                email = input("Enter your email: ")
                name = input("Enter your name: ")
                phonenumber = input("Enter your phone number: ")
            controller = UserController()
            if controller.create_user(connection, username, password, email, name, phonenumber):
                clear_screen()
                print("User created successfully")
        else:
            clear_screen()
            print("Invalid choice")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
    clear_screen()
    print("Thank you for shopping with us")

def logged_menu(type):
    # check if there are any warnings
    controller = ProductController()
    status = controller.check_all_stocks(connection)

    if type == "admin":
        print("=== Your stock status is: ", status, " ===")
        print("1. Shop")
        print("2. View Cart")
        print("3. Finish Shopping")
        print("4. Create Product")
        print("5. Delete Product")
        print("6. Check Stock")
        print("7. Logout")
        choice = int(input("Enter your choice: "))
        while choice != 7:
            if choice == 1:
                clear_screen()
                shop_menu()
            elif choice == 2:
                # view_cart()
                print("test")
            elif choice == 3:
                # finish_shopping()
                print("test")
            elif choice == 4:
                controller = ProductController()
                name = input("Enter the name of the product: ")
                brand = input("Enter the brand of the product: ")
                category = input("Enter the category of the product: ")
                price = input("Enter the price of the product: ")
                stock = input("Enter the stock of the product: ")
                while name == "" or brand == "" or category == "" or price == "" or stock == "":
                    clear_screen()
                    print("You cannot leave any fields empty")
                    name = input("Enter the name of the product: ")
                    brand = input("Enter the brand of the product: ")
                    category = input("Enter the category of the product: ")
                    price = input("Enter the price of the product: ")
                    stock = input("Enter the stock of the product: ")
                if controller.create_product(connection, price, stock, name, brand, category):
                    continue

            elif choice == 5:
                id = input("Enter the id of the product you want to delete: ")
                controller = ProductController()
                if controller.delete_product(connection, id):
                    print("Product deleted successfully")
                else:
                    print("Invalid id")
            elif choice == 6:
                controller = ProductController()
                products = controller.get_all_products_for_order(connection)
                for product in products:
                    print(product)
            else:
                print("Invalid choice")
            print("=== Your stock status is: ", status, " ===")
            print("1. Shop")
            print("2. View Cart")
            print("3. Finish Shopping")
            print("4. Create Product")
            print("5. Delete Product")
            print("6. Check Stock")
            print("7. Logout")
            choice = int(input("Enter your choice: "))
    else:
        print("1. Shop")
        print("2. View Cart")
        print("3. Finish Shopping")
        print("4. Logout")
        choice = int(input("Enter your choice: "))
        while choice != 4:
            if choice == 1:
                shop_menu()
            elif choice == 2:
                # view_cart()
                print("test")
            elif choice == 3:
                # finish_shopping()
                print("test")
            else:
                print("Invalid choice")
            print("1. Shop")
            print("2. View Cart")
            print("3. Finish Shopping")
            print("4. Logout")
            choice = int(input("Enter your choice: "))
    clear_screen()
    main_menu()
   


    

def shop_menu():
    print("1. See All Products' Categories")
    print("2. See All Products")
    print("3. Search for a Product")
    print("4. Search for a Brand")
    print("5. Go back")

    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            controller = ProductController()
            categories = controller.get_all_categories(connection)
            for category in categories:
                print(category)
        elif choice == 2:
            controller = ProductController()
            products = controller.get_all_products(connection)
            for product in products:
                print(product)

        elif choice == 3:
            controller = ProductController()
            name = input("Enter the name of the product: ")
            
            products = controller.get_product_by_name(connection, name)
            for product in products:
                print(product)
    
        elif choice == 4:
            controller = ProductController()
            brand = input("Enter the brand of the product: ")
            products = controller.get_product_by_brand(connection, brand)
            for product in products:
                print(product)
        else:
            print("Invalid choice")
        print("1. See All Products' Categories")
        print("2. See All Products")
        print("3. Search for a Product")
        print("4. Search for a Brand")
        print("5. Go back")
        choice = int(input("Enter your choice: "))
    logged_menu()

# def view_cart():
#     # print all items in cart and subtotal
#     print("1. Remove an item")
#     print("2. Go back")
#     choice = int(input("Enter your choice: "))
#     while choice != 2:
#         if choice == 1:
#             # function in controller
#         else:
#             print("Invalid choice")
#         print("1. Remove an item")
#         print("2. Go back")
#         choice = int(input("Enter your choice: "))
#     logged_menu()

# def finish_shopping():
#     print("1. Confirm")
#     print("2. Go back")
#     choice = int(input("Enter your choice: "))
#     while choice != 2:
#         if choice == 1:
#             # function in controller
#             # ask user if they want the receipt
#                 # if yes, print receipt and also save to database
#                 # if no, go back to main menu
#         else:
#             print("Invalid choice")
#         print("1. Confirm")
#         print("2. Go back")
#         choice = int(input("Enter your choice: "))
#     logged_menu()

if __name__ == "__main__":
    main()