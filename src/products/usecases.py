from products.adapter import Adapter
from tabulate import tabulate
from products.entity import ProductSelection


class UseCases():
    def create_product(self,connection, price, stock_size, name, brand, category):
        Adapter.create_product(connection, price, stock_size, name, brand, category)

    def update_product(self, connection, uuid, price, stock_size, name, brand, category):
        Adapter.update_product(connection, uuid, price, stock_size, name, brand, category)

    def delete_product(self, connection, uuid):
        Adapter.delete_product(connection, uuid)

    def get_product(self, connection, uuid):
        return Adapter.get_product(connection, uuid)

    def get_all_products(self, connection):
        return Adapter.get_all_products(connection)
    
    def get_all_products_by_category(self, connection, category):
        return Adapter.get_all_products_by_category(connection, category)

    def get_all_products_by_name(self, connection, name):
        return Adapter.get_all_products_by_name(connection, name)
    
    def get_all_products_by_brand(self, connection, brand):
        return Adapter.get_all_products_by_brand(connection, brand)

    def get_all_categories(self, connection):
        return Adapter.get_all_categories(connection)
    
    def check_all_stocks(self, connection):
        return Adapter.check_all_stocks(connection)

    def get_all_products_for_order(self, connection):
        return Adapter.get_all_products_for_order(connection)
    
    def update_stock_by_id_and_quantity(self, connection, id, quantity):
        return Adapter.update_stock_by_id_and_quantity(connection, id, quantity)

    def display_products(self, products):
        if not products:
            print("No products found")
            return

        headers = ["No.", "Product", "Brand", "Price"]
        rows = []
        for i, product in enumerate(products, start=1):
            name = product[3]  
            brand = product[4]  
            price = product[1]
            rows.append([i, name, brand, f"${price}"])

        print(tabulate(rows, headers, tablefmt="fancy_grid"))
    
    def get_product_selection(self, products, cart):
        while True:
            print("Enter the numbers of the products you want to order (comma-separated): ")
            print("Press Enter to go back")
            selected_numbers = input("Enter your choice:")
        if selected_numbers == "":
            return []
        selected_numbers = selected_numbers.replace(" ", "").split(",")
        try:
            selected_numbers = [int(num) for num in selected_numbers]
            valid_selection = all(1 <= num <= len(products) for num in selected_numbers)
            if valid_selection:
                break
            else:
                print("Invalid input. Please enter valid numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

        for num in selected_numbers:
            product = products[num - 1]
            id = product[0]
            name = product[3]  
            brand = product[4]  
            unit_price = product[1]  
            quantity = int(input(f"Enter the quantity for {name} ({brand}): "))
            cart.append(ProductSelection(id,name, brand, unit_price, quantity))

        return cart

    def print_selected_products(self, selected_products):
        for product in selected_products:
                print(f"Product: {product.name} ({product.brand})")
                print(f"Unit Price: ${product.unit_price}")
                print(f"Quantity: {product.quantity}")
                print()