import uuid
from datetime import datetime

class Product:
    def __init__(self, price, stock_size, name, brand, category):
        self.uuid = str(uuid.uuid4())
        self.price = price
        self.stock_size = stock_size
        self.name = name
        self.brand = brand
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.category = category
