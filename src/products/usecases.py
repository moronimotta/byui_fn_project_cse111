from products.adapter import Adapter
from tabulate import tabulate
from products.entity import ProductSelection


class UseCases:
    def __init__(self, connection):
        self.adapter = Adapter(connection)

    def create_product(self, price, stock_size, name, brand, category):
        return self.adapter.create_product(price, stock_size, name, brand, category)

    def delete_product(self, uuid):
        self.adapter.delete_product(uuid)

    def get_product(self, uuid):
        return self.adapter.get_product(uuid)

    def get_all_products(self):
        return self.adapter.get_all_products()
    
    def get_all_products_by_category(self, category):
        return self.adapter.get_all_products_by_category(category)

    def get_all_products_by_name(self, name):
        return self.adapter.get_all_products_by_name(name)
    
    def get_all_products_by_brand(self, brand):
        return self.adapter.get_all_products_by_brand(brand)

    def get_all_categories(self):
        return self.adapter.get_all_categories()
    
    def check_all_stocks(self):
        return self.adapter.check_all_stocks()

    def get_all_products_for_order(self):
        return self.adapter.get_all_products_for_order()
    
    def update_stock_by_id_and_quantity(self, id, quantity):
        return self.adapter.update_stock_by_id_and_quantity(id, quantity)


    def display_products(self, products):
        if not products:
            print("No products found")
            return

        headers = ["No.", "Product", "Brand", "Price", "Quantity"]
        rows = []
        for i, product in enumerate(products, start=1):
            name = product[3]  
            brand = product[4]  
            price = product[1]
            quantity = product[2]
            rows.append([i, name, brand, f"${price}", quantity])

        print(tabulate(rows, headers, tablefmt="fancy_grid"))
    
    def get_product_selection(self, products, cart):
        if not products:
            print("No products found")
            return []

        while True:
            print("Enter the numbers of the products you want to order (comma-separated): ")
            print("If you don't want to order anything, press ENTER.")
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
            max_quantity = product[2]  # Retrieve the quantity from the database
            while True:
                quantity = int(input(f"Enter the quantity for {name} ({brand}): "))
                if quantity <= max_quantity:
                    break
                else:
                    print(f"Invalid quantity. Maximum available quantity: {max_quantity}")

            cart.append(ProductSelection(id, name, brand, unit_price, quantity))

        return cart


    def print_selected_products(self, selected_products):
        for product in selected_products:
            print(f"Product: {product.name} ({product.brand})")
            print(f"Unit Price: ${product.unit_price}")
            print(f"Quantity: {product.quantity}")
            print()
