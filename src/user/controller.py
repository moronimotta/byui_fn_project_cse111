from user.adapter import Adapter

class Controller():
    def create_user(connection, username, password, email, name, phone_number):
        Adapter.create_user(connection, username, password, email, name, phone_number)

    def login(connection, username, password):
        Adapter.login(connection, username, password)

    def check_if_is_admin(username, password):
        Adapter.check_if_is_admin(username, password)