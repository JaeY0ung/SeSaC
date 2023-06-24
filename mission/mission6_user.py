import random
import csv 
import uuid

class IDGenerator:
    def generate_id(self):
        id = uuid.uuid4()
        return id
    
class NameGenerator:
    def __init__(self, file_path_sung, file_path_irum):
        self.sung = self.load_data(file_path_sung)
        self.irum = self.load_data(file_path_irum)

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read().splitlines()  # 여러줄을 가져와서 line으로 쪼개기
        return data
    
    def generate_name(self):
        sung = random.choice(self.sung)
        irum = random.choice(self.irum)
        return f"{sung}{irum}"

class GenderGenerator:
    def generate_gender(self):
        gender =  random.choice(["Male", "Female"])
        return f"{gender:>6s}"

class BirthdateGenerator:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
    def generate_birthdate(self):
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.year = random.randint(1960, 2022)
        self.month = random.choice([_ for _ in range(1,13)])
        self.day = random.randint(1, month_days[self.month-1] + 1)
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
        
class AgeGenerator:
    yearNow = 2023
    def generate_age(self, birthyear):
        return self.yearNow - birthyear + 1

class Address_Generator:
    def __init__(self, si_file_path, gu_file_path):
        self.si = self.load_data(si_file_path) # sis는 path에 있는 파일의 데이터
        self.gu = self.load_data(gu_file_path) 

    def load_data(self, file_path):  # 로드 데이터 함수는 fil_path에 있는 파일을 읽어 data에 담아 반환 하는 함수
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_address(self):
        index = random.randint(0, len(self.si)-1)
        si = self.si[index]
        gu = random.choice(self.gu[index].split(' '))
        street = random.randint(1,99)
        lo_gil = random.choice(['로','길'])
        last_num = random.randint(1,99)
        return f"{si:>4s} {gu:>4s} {street:02d}{lo_gil} {last_num:02d}"
    
class DataGenerator:
    def __init__(self, sung_file, irum_file, si_file, gu_file):   # 객체 생성
        self.id = IDGenerator()
        self.name_gen = NameGenerator(sung_file, irum_file)
        self.birthday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.age_gen = AgeGenerator()
        self.address_gen = Address_Generator(si_file, gu_file)

    def generate_data(self, count):
        data = []
        for _ in range(count):
            id = self.id.generate_id()
            name = self.name_gen.generate_name()
            birthday = self.birthday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            age = self.age_gen.generate_age(self.birthday_gen.year)
            address =self.address_gen.generate_address()
            data.append((id, name, birthday, gender, address))
        return data
    
class DataPrinter(DataGenerator): # 상속
    def print_data(self, count):
        data = self.generate_data(count)
        for id, name, birthdate, gender, address in data:
            print(f"ID:{id}\nName:{name}\nBirthdate:{birthdate}\nGender:{gender}\nAddress:{address}\n")

class DataExporter(DataGenerator):
    def exprt_to_csv(self, count, filename):
        data = self.generate_data(count)
        headers = ['ID', 'Name', 'BirthDate', 'Gender', 'Address']
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(headers)
            wr.writerows(data)
    

count_input = int(input("몇 개의 데이터를 생성하시겠습니까?: "))
sung_file = 'koreanNames_sung.txt'
irum_file = 'koreanNames_irum.txt'
city_file = 'koreaCities.txt'
si_file = 'korea_sis.txt'
gu_file = 'korea_gus.txt'
export_csv_file = 'data2.csv'

printer = DataPrinter(sung_file, irum_file, si_file, gu_file)
exporter = DataExporter(sung_file, irum_file, si_file, gu_file)

printer.print_data(count_input)
exporter.exprt_to_csv(count_input, export_csv_file)