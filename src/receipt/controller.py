
from receipt.usecases import UseCases

class Controller:
    def __init__(self, connection):
        self.connection = connection
        self.use_cases = UseCases(connection)

    def create_receipt(self, uuid, person_name, products):
        return self.use_cases.create_receipt(uuid, person_name, products)

    def get_receipt_by_uuid(self,  uuid):
        receipt = self.use_cases.get_receipt_by_uuid( uuid)
        return receipt

    def get_last_receipt_by_person_name(self, client_name):
        receipts = self.use_cases.get_last_receipt_by_person_name( client_name)
        return receipts
