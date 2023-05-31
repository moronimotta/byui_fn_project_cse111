from datetime import datetime
import uuid
from products.entity import Product
import mysql.connector

class Adapter:
    def __init__(self, connection):
        self.connection = connection

    def create_product(self, price, stock_size, name, brand, category, test=False):
        if price == "" or stock_size == "" or name == "" or brand == "" or category == "":
            print("Error: One or more fields are empty")
            return False

        try:
            cursor = self.connection.cursor()
            uuid_val = str(uuid.uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()
            product = Product(price, stock_size, name, brand, category)
            insert_query = """
            INSERT INTO products (uuid, price, stock_size, name, brand, created_at, updated_at, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (product.uuid, product.price, product.stock_size, product.name, product.brand, product.created_at, product.updated_at, product.category)
            cursor.execute(insert_query, values)
            if test:
                self.connection.rollback()
                print("Product created successfully")
            else:
                self.connection.commit()
                print("Product created successfully")
                return True
        except mysql.connector.Error as error:
            print("Error creating product:", error)
            return False

    def delete_product(self, uuid, test=False):
        try:
            cursor = self.connection.cursor()
            delete_query = """
            DELETE FROM products WHERE uuid = %s
            """
            values = (uuid,)
            cursor.execute(delete_query, values)
            if test:
                self.connection.rollback()
                print("Product deleted successfully")
            else:
                self.connection.commit()
                print("Product deleted successfully")
        except mysql.connector.Error as error:
            print("Error deleting product:", error)

    def get_product(self, uuid):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM products WHERE uuid = %s 
            """
            values = (uuid,)
            cursor.execute(select_query, values)
            products = cursor.fetchall()
            if len(products) == 0:
                print("Product not found")
                return None
            else:
                if products[0][2] == 0:
                    print("Product not available")
                    return None
                product = products[0]
                return product
        except mysql.connector.Error as error:
            print("Error retrieving product:", error)
            return None

    def get_all_products(self):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM products WHERE stock_size > 0
            """
            cursor.execute(select_query)
            products = cursor.fetchall()
            if len(products) == 0:
                print("No products found")
                return None
            else:
                return products
        except mysql.connector.Error as error:
            print("Error retrieving products:", error)
            return None

    def get_all_products_by_category(self, category):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM products WHERE category LIKE %s AND stock_size > 0
            """
            values = (category,)
            cursor.execute(select_query, values)
            products = cursor.fetchall()
            if len(products) == 0:
                print("No products found")
                return None
            else:
                return products
        except mysql.connector.Error as error:
            print("Error retrieving products by category:", error)
            return None

    def get_all_products_by_name(self, name):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM products WHERE name LIKE %s AND stock_size > 0
            """
            values = (name,)
            cursor.execute(select_query, values)
            products = cursor.fetchall()
            if len(products) == 0:
                print("No products found")
                return None
            else:
                return products
        except mysql.connector.Error as error:
            print("Error retrieving products by name:", error)
            return None

    def check_all_stocks(self):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM products WHERE stock_size <= 0
            """
            cursor.execute(select_query)
            products = cursor.fetchall()
            if len(products) > 0:
                return "DANGER = Check all stocks"
            else:
                select_query = """
                SELECT * FROM products WHERE stock_size <= 10
                """
                cursor.execute(select_query)
                products = cursor.fetchall()
                if len(products) > 0:
                    return "WARNING - Some products are running out of stock"
                else:
                    return "OK"
        except mysql.connector.Error as error:
            print("Error checking stocks:", error)
            return None

    def get_all_products_by_brand(self, brand):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM products WHERE brand LIKE %s AND stock_size > 0
            """
            values = (brand,)
            cursor.execute(select_query, values)
            products = cursor.fetchall()
            if len(products) == 0:
                print("No products found")
                return None
            else:
                return products
        except mysql.connector.Error as error:
            print("Error retrieving products by brand:", error)
            return None

    def get_all_categories(self):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT DISTINCT category FROM products
            """
            cursor.execute(select_query)
            categories = cursor.fetchall()
            if len(categories) == 0:
                print("No categories found")
                return None
            else:
                return categories
        except mysql.connector.Error as error:
            print("Error retrieving categories:", error)
            return None

    def get_all_products_for_order(self):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT name, brand, stock_size FROM products WHERE stock_size >= 0 ORDER BY stock_size ASC
            """
            cursor.execute(select_query)
            products = cursor.fetchall()
            if len(products) == 0:
                print("No products found")
                return None
            else:
                return products
        except mysql.connector.Error as error:
            print("Error retrieving products for order:", error)
            return None

    def update_stock_by_id_and_quantity(self, id, quantity, test=False):
        try:
            cursor = self.connection.cursor()
            update_query = """
            UPDATE products SET stock_size = stock_size - %s WHERE uuid = %s
            """
            values = (quantity, id)
            cursor.execute(update_query, values)
            if test:
                self.connection.rollback()
                print("Stock updated successfully")
            else:
                self.connection.commit()
                print("Stock updated successfully")
                return True
        except mysql.connector.Error as error:
            print("Error updating stock:", error)
            return False


   
        
