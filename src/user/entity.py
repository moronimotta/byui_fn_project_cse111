import uuid
from datetime import datetime

class User:
    def __init__(self, username, password, email, name, phone_number):
        self.uuid = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.phone_number = phone_number

 