import random

class storeTypeGenerator:
    def __init__(self, store_file):
        self.store_data = self.load_data(store_file)
        self.type = None

    def load_data(self, file_path):  
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_type(self):
        self.type = random.choice(self.store_data)
        return f"{self.type:>6s}"