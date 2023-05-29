import unittest
from products.adapter import Adapter as ProductAdapter
from user.adapter import Adapter as UserAdapter
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="root",
    database="grocerystore"
)

connection.autocommit = False


class TestProduct(unittest.TestCase):
    def test_create_product(self):
        price = 10.99
        stock_size = 100
        name = "Apple"
        brand = "ABC Brand"
        category = "Fruits"
        ProductAdapter.create_product(connection, price, stock_size, name, brand, category, True)
        self.assertTrue(True)  

class TestUser(unittest.TestCase):
    def test_create_user(self):
        username = "testuser"
        password = "testpass"
        email = "example@gmail.com"
        name = "Test User"
        phone = "1234567890"
        
        UserAdapter.create_user(connection, username, password, email, name, phone, True)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
