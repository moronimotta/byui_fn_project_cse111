from datetime import datetime
import uuid
from receipt.entity import Receipt
import mysql.connector
import json

class Adapter:
    def __init__(self, connection):
        self.connection = connection

    def create_receipt(self, client_name, receipt_db, client_uuid, test=False):
        try:
            cursor = self.connection.cursor()
            uuid_val = str(uuid.uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()
            insert_query = """
            INSERT INTO receipts (uuid, created_at, updated_at, client_name, receipt, client_uuid)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (uuid_val, created_at, updated_at, client_name, receipt_db, client_uuid)
            cursor.execute(insert_query, values)
            if test:
                self.connection.rollback()
                print("Receipt created successfully")
            else:
                self.connection.commit()
                print("Receipt created successfully")
                return True
        except mysql.connector.Error as error:
            print("Error creating receipt:", error)
            self.connection.rollback()
            return False

    def get_last_receipt_by_person_name(self, person_name):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT * FROM receipts WHERE client_name = %s ORDER BY created_at DESC LIMIT 1
            """
            values = (person_name,)
            cursor.execute(query, values)
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as error:
            print("Error retrieving last receipt:", error)
            return None
