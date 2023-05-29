
from datetime import datetime
import uuid
from products.entity import Product
import mysql.connector

class Adapter:
    def create_product(connection, price, stock_size, name, brand, category, test=False):
        if price == "" or stock_size == "" or name == "" or brand == "" or category == "":
            print("Error: One or more fields are empty")
            return
        cursor = connection.cursor()
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
        # check if unittest is running
        if test:
            connection.rollback()
            print("Product created successfully")
        else:
            connection.commit()
            print("Product created successfully")

    def update_product(connection, uuid, price, stock_size, name, brand, category):
        cursor = connection.cursor()
        update_query = """
        UPDATE products SET price = %s, stock_size = %s, name = %s, brand = %s, updated_at = %s, category = %s WHERE uuid = %s
        """
        updated_at = datetime.now()
        values = (price, stock_size, name, brand, updated_at, category, uuid)
        cursor.execute(update_query, values)
        connection.commit()
        print("Product updated successfully")

    def delete_product(connection, uuid):
        cursor = connection.cursor()
        delete_query = """
        DELETE FROM products WHERE uuid = %s
        """
        values = (uuid,)
        cursor.execute(delete_query, values)
        connection.commit()
        print("Product deleted successfully")

    def get_product(connection, uuid):
        cursor = connection.cursor()
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

    def get_all_products(connection):
        cursor = connection.cursor()
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

    def get_all_products_by_category(connection, category):
        cursor = connection.cursor()
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
    
    def get_all_products_by_name(connection, name):
        cursor = connection.cursor()
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

    def check_all_stocks(connection):
        cursor = connection.cursor()
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

    def get_all_products_by_brand(connection, brand):
        cursor = connection.cursor()
        select_query = """
        SELECT * FROM products WHERE brand LIKE = %s AND stock_size > 0
        """
        values = (brand,)
        cursor.execute(select_query, values)
        products = cursor.fetchall()
        if len(products) == 0:
            print("No products found")
            return None
        else:
            return products
    
    def get_all_categories(connection):
        cursor = connection.cursor()
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

    def get_all_products_for_order(connection):
        cursor = connection.cursor()
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

    def update_stock_by_id_and_quantity(connection, id, quantity):
        cursor = connection.cursor()
        update_query = """
        UPDATE products SET stock_size = stock_size - %s WHERE uuid = %s
        """
        values = (quantity, id)
        cursor.execute(update_query, values)
        connection.commit()
        print("Stock updated successfully")
        
