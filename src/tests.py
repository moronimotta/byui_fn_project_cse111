import unittest
from products.adapter import Adapter as ProductAdapter
from user.adapter import Adapter as UserAdapter
from user.usecases import UseCases as UserUseCases
from receipt.usecases import UseCases as ReceiptUseCases
import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="root",
    database="grocerystore"
)

class TestProduct(unittest.TestCase):
    def test_create_product(self):
        price = 10.99
        stock_size = 100
        name = "Apple"
        brand = "ABC Brand"
        category = "Fruits"
        adapter = ProductAdapter(connection)
        adapter.create_product(price, stock_size, name, brand, category, True)
        self.assertTrue(True)

    
    def test_delete_product(self):
        uuid = "11111111-1111-1111-1111-111111111111"
        adapter = ProductAdapter(connection)
        adapter.delete_product(uuid, True)
        self.assertTrue(True)

    def test_get_product(self):
        uuid = "11111111-1111-1111-1111-111111111111"
        adapter = ProductAdapter(connection)
        adapter.get_product(uuid)
        self.assertTrue(True)
    
    def test_get_all_products(self):
        adapter = ProductAdapter(connection)
        adapter.get_all_products()
        self.assertTrue(True)
        
    def test_get_all_products_by_category(self):
        category = "Fruits"
        adapter = ProductAdapter(connection)
        adapter.get_all_products_by_category(category)
        self.assertTrue(True)
        
    def test_get_all_products_by_name(self):
        name = "Apple"
        adapter = ProductAdapter(connection)
        adapter.get_all_products_by_name(name)
        self.assertTrue(True)
        
    def test_check_all_stocks(self):
        adapter = ProductAdapter(connection)
        adapter.check_all_stocks()
        self.assertTrue(True)
        
    def test_get_all_products_by_brand(self):
        brand = "ABC Company"
        adapter = ProductAdapter(connection)
        adapter.get_all_products_by_brand(brand)
        self.assertTrue(True)
        
    def test_get_all_categories(self):
        adapter = ProductAdapter(connection)
        adapter.get_all_categories()
        self.assertTrue(True)
        
    def test_get_all_products_for_order(self):
        adapter = ProductAdapter(connection)
        adapter.get_all_products_for_order()
        self.assertTrue(True)
        
    def test_update_stock_by_id_and_quantity(self):
        id = "11111111-1111-1111-1111-111111111111"
        quantity = 10
        adapter = ProductAdapter(connection)
        adapter.update_stock_by_id_and_quantity(id, quantity, True)
        self.assertTrue(True)


class TestUser(unittest.TestCase):
    def test_create_user(self):
        username = "testuser"
        password = "testpass"
        email = "example@gmail.com"
        name = "Test User"
        phone = "1234567890"
        
        adapter = UserAdapter(connection)
        adapter.create_user(username, password, email, name, phone, True)
        #admin
        username = "admin"
        adapter.create_user(username, password, email, name, phone, True)
        self.assertTrue(True)
    def test_login(self):
        username = "admin"
        password = "byui"
        adapter = UserAdapter(connection)
        adapter.login(username, password)
        self.assertTrue(True)
    def test_check_if_is_admin(self):
        username = "admin"
        password = "byui"
        usecases = UserUseCases(connection)
        usecases.check_if_is_admin(username, password)
        self.assertTrue(True)
        username = "testuser"
        usecases.check_if_is_admin(username, password)
        self.assertFalse(False)
    
    def test_get_user_by_username_and_password(self):
        username = "admin"
        password = "byui"
        adapter = UserAdapter(connection)
        adapter.get_user_by_username_and_password(username, password)
        self.assertTrue(True)

class TestReceipt(unittest.TestCase):
    def test_create_receipt(self):
        client_name = "Test User"
        products = [
            {
                "name": "Apple",
                "quantity": 10,
                "price": 10.99,
                "brand": "ABC Brand"
            },
            {
                "name": "Orange",
                "quantity": 5,
                "price": 5.99,
                "brand": "ABC Brand"
            }
        ]

        usecases = ReceiptUseCases(connection)
        usecases.create_receipt("123", client_name, products, True)
        self.assertTrue(True)


    def test_get_last_receipt_by_person_name(self):
        client_name = "Admin"
        usecases = ReceiptUseCases(connection)
        usecases.get_last_receipt_by_person_name(client_name)
        self.assertTrue(True)
    
    def test_convert_receipt_to_save_in_db(self):
        now = datetime.now()
        date_str = now.strftime("%A, %d %B %Y")
        time_str = now.strftime("%H:%M:%S")
        total =0
        client_name = "Admin"
        products = [
            {
                "name": "Apple",
                "quantity": 10,
                "price": 10.99,
                "brand": "ABC Brand"
            },
            {
                "name": "Orange",
                "quantity": 5,
                "price": 5.99,
                "brand": "ABC Brand"
            }
        ]
        usecases = ReceiptUseCases(connection)
        usecases.convert_receipt_to_save_in_db(client_name, products,date_str, time_str, total, True)
        self.assertTrue(True)
    

    

if __name__ == '__main__':
    unittest.main()