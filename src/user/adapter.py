from datetime import datetime
import uuid
from user.entity import User
import mysql.connector

class Adapter:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, username, password, email, name, phone_number, test=False):
        if username == "" or password == "" or email == "" or name == "" or phone_number == "":
            print("You cannot leave any fields empty")
            return False

        try:
            cursor = self.connection.cursor()
            uuid_val = str(uuid.uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()
            user = User(username, password, email, name, phone_number)
            insert_query = """
            INSERT INTO users (uuid, username, password, email, name, phone_number, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (user.uuid, user.username, user.password, user.email, user.name, user.phone_number, user.created_at, user.updated_at)
            cursor.execute(insert_query, values)
            if test:
                self.connection.rollback()
                print("User created successfully")
            else:
                self.connection.commit()
                print("User created successfully")
                return True
        except mysql.connector.Error as error:
            print("Error creating user:", error)
            return False

    def login(self, username, password):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM users WHERE username = %s AND password = %s
            """
            values = (username, password)
            cursor.execute(select_query, values)
            users = cursor.fetchall()
            if len(users) > 0:
                return True, users[0]
            else:
                print("Invalid username or password")
                return False, None
        except mysql.connector.Error as error:
            print("Error logging in:", error)
            return False, None

    def get_user_by_username_and_password(self, username, password, test=False):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM users WHERE username = %s AND password = %s
            """
            values = (username, password)
            cursor.execute(select_query, values)
            users = cursor.fetchall()
            if len(users) == 0:
                print("User not found")
                return None
            else:
                return users[0]
        except mysql.connector.Error as error:
            print("Error getting user:", error)
            return None

    def check_if_user_exists(self, username, email):
        try:
            cursor = self.connection.cursor()
            select_query = """
            SELECT * FROM users WHERE username = %s OR email = %s
            """
            values = (username, email)
            cursor.execute(select_query, values)
            users = cursor.fetchall()
            if len(users) == 0:
                return False
            else:
                return True
        except mysql.connector.Error as error:
            print("Error checking user existence:", error)
            return False
