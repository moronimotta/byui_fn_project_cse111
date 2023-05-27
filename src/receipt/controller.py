from receipt.adapter import Adapter

class Controller():
    def create_receipt(connection, client_name, total, payment_method, payment_date, items):
        Adapter.create_receipt(connection, client_name, total, payment_method, payment_date, items)

    def get_all_receipts(connection):
        receipts = Adapter.get_all_receipts(connection)
        return receipts

    def get_receipt_by_uuid(connection, uuid):
        receipt = Adapter.get_receipt_by_uuid(connection, uuid)
        return receipt

    def update_receipt(connection, uuid, client_name, total, payment_method, payment_date, items):
        Adapter.update_receipt(connection, uuid, client_name, total, payment_method, payment_date, items)

    def delete_receipt(connection, uuid):
        Adapter.delete_receipt(connection, uuid)

    def get_receipts_by_client_name(connection, client_name):
        receipts = Adapter.get_receipts_by_client_name(connection, client_name)
        return receipts