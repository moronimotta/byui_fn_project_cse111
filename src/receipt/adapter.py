from datetime import datetime
import uuid
from receipt.entity import Receipt
import mysql.connector

def create_receipt(connection, client_name, total, payment_method, payment_date, items):
    cursor = connection.cursor()
    uuid_val = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    receipt = Receipt(client_name, total, payment_method, payment_date, items)
    insert_query = """
    INSERT INTO receipts (uuid, client_name, total, payment_method, payment_date, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (receipt.uuid, receipt.client_name, receipt.total, receipt.payment_method, receipt.payment_date, receipt.created_at, receipt.updated_at)
    cursor.execute(insert_query, values)
    connection.commit()
    print("Receipt created successfully")

def get_all_receipts(connection):
    cursor = connection.cursor()
    select_query = """
    SELECT * FROM receipts
    """
    cursor.execute(select_query)
    receipts = cursor.fetchall()
    return receipts

def get_receipt_by_uuid(connection, uuid):
    cursor = connection.cursor()
    select_query = """
    SELECT * FROM receipts WHERE uuid = %s
    """
    values = (uuid,)
    cursor.execute(select_query, values)
    receipt = cursor.fetchone()
    return receipt

def update_receipt(connection, uuid, client_name, total, payment_method, payment_date, items):
    cursor = connection.cursor()
    updated_at = datetime.now()
    receipt = Receipt(client_name, total, payment_method, payment_date, items)
    update_query = """
    UPDATE receipts SET client_name = %s, total = %s, payment_method = %s, payment_date = %s, updated_at = %s WHERE uuid = %s
    """
    values = (receipt.client_name, receipt.total, receipt.payment_method, receipt.payment_date, receipt.updated_at, uuid)
    cursor.execute(update_query, values)
    connection.commit()
    print("Receipt updated successfully")

def delete_receipt(connection, uuid):
    cursor = connection.cursor()
    delete_query = """
    DELETE FROM receipts WHERE uuid = %s
    """
    values = (uuid,)
    cursor.execute(delete_query, values)
    connection.commit()
    print("Receipt deleted successfully")

def get_receipts_by_client_name(connection, client_name):
    cursor = connection.cursor()
    select_query = """
    SELECT * FROM receipts WHERE client_name = %s
    """
    values = (client_name,)
    cursor.execute(select_query, values)
    receipts = cursor.fetchall()
    return receipts

