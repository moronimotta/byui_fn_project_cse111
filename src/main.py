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
    host="localhost",
    user="admin",
    password="root",
    database="grocerystore"
)

if connection.is_connected():
    print("Connected to MySQL database")

def main():
    clear_screen()

    main_menu()

    connection.close()

def empty_cart(cart):
    cart = []
    return cart


def view_cart(cart):
    if not cart:
        print("Your cart is empty")
        return

    headers = ["Product", "Brand", "Unit Price", "Quantity", "Subtotal"]
    rows = []
    subtotal = 0
    for product in cart:
        subtotal = product.unit_price * product.quantity
        rows.append([product.name, product.brand, f"${product.unit_price}", product.quantity, f"${subtotal}"])

    print(tabulate(rows, headers, tablefmt="fancy_grid"))

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
            controller = UserController()
            lgn_succ, type = controller.login(connection, usrname, password)
            if lgn_succ:
                clear_screen()
                print("Login successful")
                login_info.append(usrname)
                login_info.append(password)
                logged_menu(type)
                print("Thank you for shopping with us")
                break
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
            controller = UserController()
            if controller.create_user(connection, username, password, email, name, phonenumber):
                clear_screen()
                print("User created successfully")
            print("Login in to continue")
            usrname = input("Enter your username: ")
            password = input("Enter your password: ")
            controller = UserController()
            lgn_succ, type = controller.login(connection, usrname, password)
            if lgn_succ:
                clear_screen()
                print("Login successful")
                login_info.append(usrname)
                login_info.append(password)
                logged_menu(type)
                print("Thank you for shopping with us")
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
    print("Thank you for shopping with us")


def logged_menu(type):
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
            clear_screen()
            if choice == 1:
                shop_menu()
            elif choice == 2:
                view_cart(cart)
            elif choice == 3:
                finish_shopping()
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
            elif choice == 6:
                clear_screen()
                controller = ProductController()
                products = controller.get_all_products_for_order(connection)

                headers = ["Product", "Quantity"]
                rows = [[product[0], product[2]] for product in products]

                print(tabulate(rows, headers, tablefmt="fancy_grid"))
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
            print("7. Logout")
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
            controller = ProductController()
            categories = controller.get_all_categories(connection)

            headers = ["Category"]
            rows = [[category[0]] for category in categories]

            print(tabulate(rows, headers, tablefmt="fancy_grid"))
        elif choice == 2:
            controller = ProductController()
            products = controller.get_all_products(connection)

            display_products(products)

            product_selection = controller.get_product_selection(products, cart)

            clear_screen()

            controller.print_selected_products(product_selection)
        elif choice == 3:
            controller = ProductController()
            name = input("Enter the name of the product: ")
            products = controller.get_all_products_by_name(connection, name)

            display_products(products)

            product_selection = controller.get_product_selection(products, cart)

            clear_screen()

            controller.print_selected_products(product_selection)
        elif choice == 4:
            controller = ProductController()
            brand = input("Enter the brand of the product: ")
            products = controller.get_product_by_brand(connection, brand)
            for product in products:
                print(product)
        elif choice == 5:
            empty_cart(cart)
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
            pdt_controller = ProductController()
            usr_controller = UserController()
            user_account = usr_controller.get_user_by_username_and_password(connection, login_info[0], login_info[1])

            person_name = user_account[6]
            products = []
            for product in cart:
                product_info = {
                    "name": product.name,
                    "brand": product.brand,
                    "price": product.unit_price * product.quantity,
                    "quantity": product.quantity,
                }
                products.append(product_info)

            if create_grocery_receipt(person_name, products):
                for product in cart:
                    pdt_controller.update_stock_by_id_and_quantity(connection, product.id, product.quantity)
                empty_cart(cart)
                print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice")

        clear_screen()
        print("Are you sure you want to finish shopping?")
        print("1. Confirm")
        print("2. Go back")
        choice = int(input("Enter your choice: "))


def create_grocery_receipt(person_name, products):
    now = datetime.now()
    date_str = now.strftime("%A, %d %B %Y")
    time_str = now.strftime("%H:%M:%S")

    # ensure that you are running this script from the root directory of the project
    directory = "user_receipts"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = f"{directory}/{person_name}_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    headers = ["No.", "Product", "Brand", "Price", "Quantity"]
    rows = []
    total = 0
    for i, product in enumerate(products, start=1):
        name = product["name"]
        brand = product["brand"]
        price = product["price"]
        quantity = product["quantity"]
        rows.append([i, name, brand, f"${price}", quantity])
        total += price

    rows.append(["", "", "Total", f"${total}"])

    receipt_content = f"Grocery Receipt\n\nPerson's Name: {person_name}\nDate: {date_str}\nTime: {time_str}\n\n"
    receipt_content += tabulate(rows, headers, tablefmt="fancy_grid")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(receipt_content)

    print(f"\nReceipt saved as '{filename}'")


def send_receipt_to_db():
    # call controller
    
    json = {
        "person_name": variable,
        "date": variable,
        "time": variable,
        "products": [
            {
                "name": variable,
                "brand": variable,
                "price": variable,
                "quantity": variable,
            },
        ]
    }
    # call function

if __name__ == "__main__":
    main()



