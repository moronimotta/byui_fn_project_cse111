from products.adapter import Adapter

class Controller():
    def create_product(connection, price, stock_size, name, company, category):
        Adapter.create_product(connection, price, stock_size, name, company, category)

    def update_product(connection, uuid, price, stock_size, name, company, category):
        Adapter.update_product(connection, uuid, price, stock_size, name, company, category)

    def delete_product(connection, uuid):
        Adapter.delete_product(connection, uuid)

    def get_product(connection, uuid):
        return Adapter.get_product(connection, uuid)

    def get_all_products(connection):
        return Adapter.get_all_products(connection)
    
    def get_all_products_by_category(connection, category):
        return Adapter.get_all_products_by_category(connection, category)

    def get_all_products_by_name(connection, name):
        return Adapter.get_all_products_by_name(connection, name)
