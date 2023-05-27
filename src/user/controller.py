from user.adapter import Adapter

class Controller:
    def create_user(self, connection, username, password, email, name, phone_number):
        Adapter.create_user(connection, username, password, email, name, phone_number)

    def login(self, connection, username, password):
        success, user_type = Adapter.login(connection, username, password)
        if success:
            return success, user_type
        else:
            return False, None

