class Cart:
    def __init__(self, product_name, unit_price, quantity, total_price):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.total_price = total_price
        
    def __str__(self):
        return f"{self.product_name} - {self.unit_price} - {self.quantity} - {self.total_price}"


   

    