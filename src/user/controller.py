from user.usecases import UseCases

class Controller:
    def __init__(self, connection):
        self.connection = connection
        self.use_cases = UseCases(connection)

    def create_user(self, username, password, email, name, phone_number):
        return self.use_cases.create_user(username, password, email, name, phone_number)

    def login(self, username, password):
        success, user_type = self.use_cases.login(username, password)
        if success:
            return success, user_type
        else:
            return False, None
    
    def get_user_by_username_and_password(self, username, password):
        return self.use_cases.get_user_by_username_and_password(username, password)

