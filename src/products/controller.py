from products.adapter import Adapter

class Controller():
    def create_product(self,connection, price, stock_size, name, brand, category):
        Adapter.create_product(connection, price, stock_size, name, brand, category)

    def update_product(self, connection, uuid, price, stock_size, name, brand, category):
        Adapter.update_product(connection, uuid, price, stock_size, name, brand, category)

    def delete_product(self, connection, uuid):
        Adapter.delete_product(connection, uuid)

    def get_product(self, connection, uuid):
        return Adapter.get_product(connection, uuid)

    def get_all_products(self, connection):
        return Adapter.get_all_products(connection)
    
    def get_all_products_by_category(self, connection, category):
        return Adapter.get_all_products_by_category(connection, category)

    def get_all_products_by_name(self, connection, name):
        return Adapter.get_all_products_by_name(connection, name)
    
    def get_all_products_by_brand(self, connection, brand):
        return Adapter.get_all_products_by_brand(connection, brand)

    def get_all_categories(self, connection):
        return Adapter.get_all_categories(connection)
    
    def check_all_stocks(self, connection):
        return Adapter.check_all_stocks(connection)

    def get_all_products_for_order(self, connection):
        return Adapter.get_all_products_for_order(connection)
    
    def update_stock_by_id_and_quantity(self, connection, id, quantity):
        Adapter.update_stock_by_id_and_quantity(connection, id, quantity)