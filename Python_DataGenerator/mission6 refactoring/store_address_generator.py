import random

class StoreAddressGenerator:
    def __init__(self, si_file_path, gu_file_path):
        self.si_data = self.load_data(si_file_path) # sis는 path에 있는 파일의 데이터
        self.gu_data = self.load_data(gu_file_path)
        self.gu = None

    def load_data(self, file_path):  # 로드 데이터 함수는 fil_path에 있는 파일을 읽어 data에 담아 반환 하는 함수
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_address(self):
        index = random.randint(0, len(self.si_data)-1)
        si = self.si_data[index]
        self.gu = random.choice(self.gu_data[index].split(' '))
        street = str(random.randint(1,99))
        lo_gil = random.choice(['로','길'])
        last_num = str(random.randint(1,99))
        return f"{si:>4s} {self.gu:>4s} {street:>2s}{lo_gil} {last_num:>2s}"