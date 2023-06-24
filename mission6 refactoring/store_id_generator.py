import uuid

class StoreIDGenerator:
    def generate_id(self):
        id = uuid.uuid4()
        return id