import uuid

class Product:
    def __init__(self, price, stock_size, name, company, category):
        self.uuid = str(uuid.uuid4())
        self.price = price
        self.stock_size = stock_size
        self.name = name
        self.company = company
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.category = category
