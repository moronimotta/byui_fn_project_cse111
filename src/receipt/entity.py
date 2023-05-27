import uuid
from datetime import datetime

class Receipt:
    def __init__(self, client_name, total, payment_method, payment_date, items):
        self.uuid = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        self.client_name = client_name
        self.total = total
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.items = items

 