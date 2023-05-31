import uuid
from datetime import datetime
import mysql.connector
from receipt.controller import Controller as ReceiptController
from products.controller import Controller as ProductController
from user.controller import Controller as UserController
from tabulate import tabulate
import os

cart = []
login_info = []


# connect to database
connection = mysql.connector.connect(
    host="db_local_byui",
    user="admin",
    password="root",
    database="grocerystore"
)



def main():
    clear_screen()

    main_menu()

    connection.close()

def empty_cart():
    global cart
    cart = []


def view_cart(cart):
    if not cart:
        print("Your cart is empty")
        return

    headers = ["Product", "Brand", "Unit Price", "Quantity", "Subtotal"]
    rows = []
    total = 0
    for product in cart:
        subtotal = product.unit_price * product.quantity
        rows.append([product.name, product.brand, f"${product.unit_price}", product.quantity, f"${subtotal}"])
        total += subtotal

    print(tabulate(rows, headers, tablefmt="fancy_grid"))
    print(f"Total: ${total}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    clear_screen()
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
            controller = UserController(connection)
            lgn_succ, user_type = controller.login(usrname, password)
            if lgn_succ:
                clear_screen()
                print("Login successful")
                global login_info 
                login_info = [usrname, password]
                logged_menu(user_type)
                print("Come back soon!")
                break
            else:
                clear_screen()
                print("Invalid username or password")
        elif choice == 2:
            clear_screen()
            ok = False
            while ok != True:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                email = input("Enter your email: ")
                name = input("Enter your name: ")
                phonenumber = input("Enter your phone number: ")
                controller = UserController(connection)
                ok = controller.create_user(username, password, email, name, phonenumber)
                if ok:
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print("Invalid username or email")
            print("Log in to continue")
            while True:
                usrname = input("Enter your username: ")
                password = input("Enter your password: ")
                controller = UserController(connection)
                login_success, user_type = controller.login(usrname, password)
                if login_success:
                    break
                else:
                    clear_screen()
                    print("Invalid username or password")
        else:
            clear_screen()
            print("Invalid choice")
        
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

    clear_screen()
    print("Come back soon!")


def logged_menu(type):
    controller = ProductController(connection)
    status = controller.check_all_stocks()

    if type == "admin":
        print("=== Your stock status is: ", status, " ===")
        print("1. Shop")
        print("2. View Cart")
        print("3. Finish Shopping")
        print("4. Create Product")
        print("5. Delete Product")
        print("6. Check Stock")
        print("7. Check Receipt From Client")
        print("8. Logout")
        choice = int(input("Enter your choice: "))
        while choice != 8:
            clear_screen()
            if choice == 1:
                shop_menu()
            elif choice == 2:
                view_cart(cart)
            elif choice == 3:
                finish_shopping()
            elif choice == 4:
                controller = ProductController(connection)
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
                if controller.create_product(price, stock, name, brand, category):
                    continue

            elif choice == 5:
                id = input("Enter the id of the product you want to delete: ")
                controller = ProductController(connection)
                if controller.delete_product(id):
                    print("Product deleted successfully")
            elif choice == 6:
                clear_screen()
                controller = ProductController(connection)
                products = controller.get_all_products_for_order()

                headers = ["Product", "Quantity"]
                rows = [[product[0], product[2]] for product in products]

                print(tabulate(rows, headers, tablefmt="fancy_grid"))
            elif choice == 7:
                clear_screen()
                client_name = input("Enter the full name of the person: ")
                controller = ReceiptController(connection)
                controller.get_last_receipt_by_person_name(client_name)         
            else:
                print("Invalid choice")
            input("Press Enter to continue...")
            clear_screen()
            print("=== Your stock status is: ", status, " ===")
            print("1. Shop")
            print("2. View Cart")
            print("3. Finish Shopping")
            print("4. Create Product")
            print("5. Delete Product")
            print("6. Check Stock")
            print("7. Check Receipt From Client")
            print("8. Logout")
            choice = int(input("Enter your choice: "))
    else:
        print("1. Shop")
        print("2. View Cart")
        print("3. Finish Shopping")
        print("4. Logout")
        choice = int(input("Enter your choice: "))
        while choice != 4:
            clear_screen()
            if choice == 1:
                shop_menu()
            elif choice == 2:
                view_cart(cart)
            elif choice == 3:
                finish_shopping()
            else:
                print("Invalid choice")
            input("Press Enter to continue...")
            clear_screen()
            print("1. Shop")
            print("2. View Cart")
            print("3. Finish Shopping")
            print("4. Logout")
            choice = int(input("Enter your choice: "))
    
    clear_screen()

def shop_menu():
    print("1. See All Products' Categories")
    print("2. See All Products")
    print("3. Search for a Product")
    print("4. Search for a Brand")
    print("5. Empty Cart")
    print("6. Go back")

    choice = int(input("Enter your choice: "))
    while choice != 6:
        clear_screen()
        if choice == 1:
            controller = ProductController(connection)
            categories = controller.get_all_categories()

            headers = ["Category"]
            rows = [[category[0]] for category in categories]

            print(tabulate(rows, headers, tablefmt="fancy_grid"))
        elif choice == 2:
            controller = ProductController(connection)
            products = controller.get_all_products()

            controller.display_products(products)

            product_selection = controller.get_product_selection(products, cart)

            clear_screen()

            controller.print_selected_products(product_selection)
        elif choice == 3:
            controller = ProductController(connection)
            name = input("Enter the name of the product: ")
            products = controller.get_all_products_by_name(name)

            controller.display_products(products)

            product_selection = controller.get_product_selection(products, cart)

            clear_screen()

            controller.print_selected_products(product_selection)
        elif choice == 4:
            controller = ProductController(connection)
            brand = input("Enter the brand of the product: ")
            products = controller.get_all_products_by_brand(brand)
            if products:
                controller.display_products(products)
                product_selection= controller.get_product_selection(products, cart)
                    
        elif choice == 5:
            empty_cart()
        else:
            print("Invalid choice")
        input("Press Enter to continue...")
        clear_screen()
        print("1. See All Products' Categories")
        print("2. See All Products")
        print("3. Search for a Product")
        print("4. Search for a Brand")
        print("5. Empty Cart")
        print("6. Go back")
        choice = int(input("Enter your choice: "))


def finish_shopping():
    if not cart:
        print("Your cart is empty")
        return

    view_cart(cart)
    print("Are you sure you want to finish shopping?")
    print("1. Confirm")
    print("2. Go back")
    choice = int(input("Enter your choice: "))
    while choice != 2:
        if choice == 1:
            pdt_controller = ProductController(connection)
            usr_controller = UserController(connection)
            user_account = usr_controller.get_user_by_username_and_password(login_info[0], login_info[1])
            if user_account is None:
                return
            else: 
                person_name = user_account[6]
                uuid = user_account[0]
                products = []
                for product in cart:
                    product_info = {
                        "name": product.name,
                        "brand": product.brand,
                        "price": product.unit_price * product.quantity,
                        "quantity": product.quantity,
                    }
                    products.append(product_info)

                rcpt_controller = ReceiptController(connection)
                
                rcpt_controller.create_receipt(uuid,person_name, products)
                for product in cart:
                    pdt_controller.update_stock_by_id_and_quantity(product.id, product.quantity)
                empty_cart()
                print("Thank you for shopping with us!")
                break
        else:
            print("Invalid choice")

        clear_screen()
        print("Are you sure you want to finish shopping?")
        print("1. Confirm")
        print("2. Go back")
        choice = int(input("Enter your choice: "))



if __name__ == "__main__":
    main()



