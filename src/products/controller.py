from products.usecases import UseCases

class Controller():
    def create_product(self,connection, price, stock_size, name, brand, category):
        UseCases.create_product(connection, price, stock_size, name, brand, category)

    def update_product(self, connection, uuid, price, stock_size, name, brand, category):
        UseCases.update_product(connection, uuid, price, stock_size, name, brand, category)

    def delete_product(self, connection, uuid):
        UseCases.delete_product(connection, uuid)

    def get_product(self, connection, uuid):
        return UseCases.get_product(connection, uuid)

    def get_all_products(self, connection):
        return UseCases.get_all_products(connection)
    
    def get_all_products_by_category(self, connection, category):
        return UseCases.get_all_products_by_category(connection, category)

    def get_all_products_by_name(self, connection, name):
        return UseCases.get_all_products_by_name(connection, name)
    
    def get_all_products_by_brand(self, connection, brand):
        return UseCases.get_all_products_by_brand(connection, brand)

    def get_all_categories(self, connection):
        return UseCases.get_all_categories(connection)
    
    def check_all_stocks(self, connection):
        return UseCases.check_all_stocks(connection)

    def get_all_products_for_order(self, connection):
        return UseCases.get_all_products_for_order(connection)
    
    def update_stock_by_id_and_quantity(self, connection, id, quantity):
        UseCases.update_stock_by_id_and_quantity(connection, id, quantity)
    
    def display_products(self, products):
        return UseCases.display_products(products)
    
    def get_product_selection(self, products, cart):
        return UseCases.get_product_selection(products, cart)
    
    def print_selected_products(self, products):
        return UseCases.print_selected_products(products)
    

