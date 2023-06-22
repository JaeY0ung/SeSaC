import random
import csv 
import uuid
# TODO dsafsfsa
class StoreIDGenerator:
    def generate_id(self):
        id = uuid.uuid4()
        return id
    
class StoreNameGenerator:
    def generate_name(self, type, gu):
        ho = random.randint(1, 9)
        return f"{type:>6s} {gu:>4s}{ho}호점"
    
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
    
class DataGenerator:
    def __init__(self, storeName_file, si_file, gu_file):   # 객체 생성
        self.store_id_gen = StoreIDGenerator()
        self.store_name_gen = StoreNameGenerator()
        self.store_address_gen = StoreAddressGenerator(si_file, gu_file)
        self.store_type_gen = storeTypeGenerator(storeName_file)

    def generate_data(self, count):
        data = []
        for _ in range(count):
            id = self.store_id_gen.generate_id()
            type = self.store_type_gen.generate_type()
            address = self.store_address_gen.generate_address()
            gu = self.store_address_gen.gu
            name = self.store_name_gen.generate_name(type,gu)
            data.append((id, name, type, address))
        return data
    
class DataPrinter(DataGenerator): # 상속
    def exprt_to_console(self, count):
        data = self.generate_data(count)
        for id, name, type, address in data:
            print(f"ID:{id}\nName:{name}\nType:{type}\nAddress:{address}\n")
    
    def exprt_to_csv(self, count, filename):
        data = self.generate_data(count)
        headers = ['ID', 'Name', 'Type', 'Address']
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(headers)
            wr.writerows(data)

count_input = int(input("몇 개의 데이터를 생성하시겠습니까?: "))
storeName_file = 'storeNames.txt'
city_file = 'koreaCities.txt'
si_file = 'korea_sis.txt'
gu_file = 'korea_gus.txt'
export_csv_file = 'data2.csv'

while True:
    print_or_csv = input("print or csv?: ").lower()
    exporter = DataPrinter(storeName_file, si_file, gu_file)
    if print_or_csv == 'print':
        exporter.exprt_to_console(count_input)
        break
    elif print_or_csv == 'csv':
        exporter.exprt_to_csv(count_input, export_csv_file)
        break
    print("잘못 입력하셨습니다. 다시 입력해 주세요.")