import random

class StoreNameGenerator:
    def generate_name(self, type, gu):
        ho = random.randint(1, 9)
        return f"{type:>6s} {gu:>4s}{ho}호점"