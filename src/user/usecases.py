from user.adapter import Adapter

class UseCases:
    def __init__(self, connection):
        self.connection = connection
        self.adapter = Adapter(connection)
    
    def create_user(self, username, password, email, name, phone_number):
        if self.adapter.check_if_user_exists(username, email):
            return
        else:
            return self.adapter.create_user(username, password, email, name, phone_number)
        
    def login(self, username, password):
        bool, user = self.adapter.login(username, password)
        if bool:
            if self.check_if_is_admin(username, password):
                    return True, "admin",
            else:
                    return True, "user"
        else:
            return False, None
    
    def get_user_by_username_and_password(self, username, password):
        return self.adapter.get_user_by_username_and_password(username, password)
        
    def check_if_is_admin(self, username, password):
        if username == "admin" and password == "byui":
            return True
        else:
            print("Invalid username or password")
            return False
