import uuid
from datetime import datetime

class Receipt:
    def __init__(self, client_name, client_uuid, receipt):
        self.uuid = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.client_name = client_name
        self.receipt =  receipt
        self.client_uuid = client_uuid

 