from datetime import datetime
import uuid
from user.entity import User
import mysql.connector

class Adapter:
    def create_user(connection, username, password, email, name, phone_number):
        if username == "" or password == "" or email == "" or name == "" or phone_number == "":
            print("You cannot leave any fields empty")
            return
        cursor = connection.cursor()
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
        connection.commit()
        print("User created successfully")


    def login(connection, username, password):
        cursor = connection.cursor()
        select_query = """
        SELECT * FROM users WHERE username = %s AND password = %s
        """
        values = (username, password)
        cursor.execute(select_query, values)
        users = cursor.fetchall()
        if len(users) > 0:
            if Adapter.check_if_is_admin(username, password):
                return True, "admin",
            else:
                return True, "user"
        else:
            print("Invalid username or password")
            return False, None
            

    def check_if_is_admin(username, password):
        if username == "admin" and password == "byui":
            return True
        else:
            print("Invalid username or password")
            return False



    