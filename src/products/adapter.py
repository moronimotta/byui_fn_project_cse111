
from datetime import datetime
import uuid
from products.entity import Product
import mysql.connector

class Adapter:
    def create_product(connection, price, stock_size, name, company, category):
        cursor = connection.cursor()
        uuid_val = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        product = Product(price, stock_size, name, company, category)
        insert_query = """
        INSERT INTO products (uuid, price, stock_size, name, company, created_at, updated_at, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (product.uuid, product.price, product.stock_size, product.name, product.company, product.created_at, product.updated_at, product.category)
        cursor.execute(insert_query, values)
        connection.commit()
        print("Product created successfully")

    def update_product(connection, uuid, price, stock_size, name, company, category):
        cursor = connection.cursor()
        update_query = """
        UPDATE products SET price = %s, stock_size = %s, name = %s, company = %s, updated_at = %s, category = %s WHERE uuid = %s
        """
        updated_at = datetime.now()
        values = (price, stock_size, name, company, updated_at, category, uuid)
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
            product = products[0]
            return product

    def get_all_products(connection):
        cursor = connection.cursor()
        select_query = """
        SELECT * FROM products
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
        SELECT * FROM products WHERE category = %s
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
        SELECT * FROM products WHERE name = %s
        """
        values = (name,)
        cursor.execute(select_query, values)
        products = cursor.fetchall()
        if len(products) == 0:
            print("No products found")
            return None
        else:
            return products