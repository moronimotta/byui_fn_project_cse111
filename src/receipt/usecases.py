from receipt.adapter import Adapter
from tabulate import tabulate
import os
from datetime import datetime
import json
from decimal import Decimal
class UseCases:
    def __init__(self, connection):
        self.connection = connection
        self.adapter = Adapter(connection)
    
    def create_receipt(self, uuid,  person_name, products, test=False):
        receipt_db = self.create_grocery_receipt_to_save_local(person_name, products, test)
        return self.adapter.create_receipt(person_name,receipt_db,uuid)
    
    def get_last_receipt_by_person_name(self, person_name):
        result = self.adapter.get_last_receipt_by_person_name(person_name)
        if result is None:
            print(f"Receipt for '{person_name}' not found")
            return
        receipt_json = result[4].replace("'", '"')

        receipt_data = json.loads(receipt_json)
        
        products = receipt_data["products"]
        total = receipt_data["total"]
        
        headers = ["Product", "Brand", "Unit Price", "Quantity", "Subtotal"]
        rows = []
        for product in products:
            name = product["name"]
            brand = product["brand"]
            price = product["price"]
            quantity = product["quantity"]
            unit_price = float(price) / quantity
            rows.append([name, brand, f"${unit_price}", quantity, f"${price}"])


        rows.append(["", "", "", "Total", f"${total}"])

        print(tabulate(rows, headers, tablefmt="fancy_grid"))


    def create_grocery_receipt_to_save_local(self, person_name, products, test=False):
        now = datetime.now()
        date_str = now.strftime("%A, %d %B %Y")
        time_str = now.strftime("%H:%M:%S")

        

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

        # ensure that you are running this script from the root directory of the project
        directory = "user_receipts"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = f"{directory}/{person_name}_{now.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(receipt_content)
        if test:
            os.remove(filename)
            return
        print(f"\nReceipt saved as '{filename}'")
        receipt_db = self.convert_receipt_to_save_in_db(person_name, products, date_str, time_str, total)
        return receipt_db

    def convert_receipt_to_save_in_db(self, person_name, products, date_str, time_str, total, test=False):
        
        converted_products = []
        for product in products:
            converted_product = {
                "name": product["name"],
                "brand": product["brand"],
                "price": str(product["price"]),
                "quantity": product["quantity"]
            }
            converted_products.append(converted_product)

   
        receipt = {
            "person_name": person_name,
            "products": converted_products,
            "date": date_str,
            "time": time_str,
            "total": str(total)
        }

        receipt_json = json.dumps(receipt)
        if test:
            return True
        return receipt_json



    