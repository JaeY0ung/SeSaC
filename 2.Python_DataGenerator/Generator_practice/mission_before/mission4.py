import random
import csv 

class NameGenerator:
    def __init__(self, file_path):
        self.names = self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read().splitlines()  # 여러줄을 가져와서 line으로 쪼개기
        return data
    
    def generate_name(self):
        return random.choice(self.names)

class GenderGenerator:
    def generate_gender(self):
        return random.choice(["Male", "Female"])

class BirthdateGenerator:
    def generate_birthdate(self):
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        year = random.randint(1960, 2022)
        month = random.choice([_ for _ in range(1,13)])
        day = random.randint(1, month_days[month-1] + 1)
        return f"{year}-{month:02d}-{day:02d}"
        
class YearGenerator:
    yearNow = 2023
    def generate_age(self, birthyear):
        return self.yearNow - birthyear + 1

class Address_Generator:
    def __init__(self,file_path):
         self.cities = self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path,"r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1,100)
        return f"{street} {city}"
    
class DataGenerator:
    def __init__(self,name_file,city_file):   # 객체 생성
        self.name_gen = NameGenerator(name_file)
        self.birthday_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = Address_Generator(city_file)

    def generate_data(self,count):
        data = []
        for _ in range(count):
            name = self.name_gen.generate_name()
            birthday = self.birthday_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address =self.address_gen.generate_address()
            data.append((name,birthday,gender,address))
        return data
    
class DataPrinter(DataGenerator): # 상속
    def print_data(self, count):
        data = self.generate_data(count)
        for name,birthdate,gender,address in data:
            print(f"Name:{name}\nBirthdate:{birthdate}\nGender:{gender}\nAddress:{address}")

class DataExporter(DataGenerator):
    def exprt_to_csv(self,count,filename):
        data = self.generate_data(count)
        headers = ['Name','BirthDate','Gender','Address']
        with open(filename,'w',newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(headers)
            wr.writerows(data)
    
name_file = 'names.txt'
city_file = 'cities.txt'
printer = DataPrinter(name_file, city_file)
exporter = DataExporter(name_file,city_file)
printer.print_data(100)

exporter.exprt_to_csv(100,'data.csv')