from products.usecases import UseCases

class Controller:
    def __init__(self, connection):
        self.connection = connection
        self.use_cases = UseCases(connection)

    def create_product(self, price, stock_size, name, brand, category):
        return self.use_cases.create_product(price, stock_size, name, brand, category)

    def update_product(self, uuid, price, stock_size, name, brand, category):
        self.use_cases.update_product(uuid, price, stock_size, name, brand, category)

    def delete_product(self, uuid):
        self.use_cases.delete_product(uuid)

    def get_product(self, uuid):
        return self.use_cases.get_product(uuid)

    def get_all_products(self):
        return self.use_cases.get_all_products()
    
    def get_all_products_by_category(self, category):
        return self.use_cases.get_all_products_by_category(category)

    def get_all_products_by_name(self, name):
        return self.use_cases.get_all_products_by_name(name)
    
    def get_all_products_by_brand(self, brand):
        return self.use_cases.get_all_products_by_brand(brand)

    def get_all_categories(self):
        return self.use_cases.get_all_categories()

    def check_all_stocks(self):
        return self.use_cases.check_all_stocks()

    def get_all_products_for_order(self):
        return self.use_cases.get_all_products_for_order()
    
    def update_stock_by_id_and_quantity(self, id, quantity):
        return self.use_cases.update_stock_by_id_and_quantity(id, quantity)
    
    def display_products(self, products):
        return self.use_cases.display_products(products)
    
    def get_product_selection(self, products, cart):
        return self.use_cases.get_product_selection(products, cart)
    
    def print_selected_products(self, products):
        return self.use_cases.print_selected_products(products)

    

