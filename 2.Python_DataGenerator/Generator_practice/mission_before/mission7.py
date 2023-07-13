import random
import csv 
import uuid
import datetime

class IDGenerator:
    userid = None
    storeid = None

    def generate_userid(self):
        self.userid = uuid.uuid4()
        return self.userid
    
    def generate_storeid(self):
        self.storeid = uuid.uuid4()
        return self.storeid

class NameGenerator:
    def __init__(self):
        self.userfullname = None
        self.storename = None

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read().splitlines()  # 여러줄을 가져와서 line으로 쪼개기
        return data
    
    def generate_username(self, file_sung, file_irum):
        sung_data = self.load_data(file_sung)
        irum_data = self.load_data(file_irum)
        usersung = random.choice(sung_data)
        userirum = random.choice(irum_data)
        self.userfullname = f"{usersung}{userirum}"
        return self.userfullname
    
    def generate_storename(self, type, gu):
        ho = random.randint(1, 9)
        self.storename = f"{type:>6s} {gu:>4s}{ho}호점"
        return self.storename

class GenderGenerator:
    def __init__(self):
        self.usergender = None

    def generate_gender(self):
        self.usergender =  random.choice(["Male", "Female"])
        return f"{self.usergender:>6s}"

class BirthdateGenerator:
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0

    def generate_birthdate(self):
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.year = random.randint(1960, 2022)
        self.month = random.choice([_ for _ in range(1,13)])
        self.day = random.randint(1, month_days[self.month-1] + 1)
        birthdate = f"{self.year}-{self.month:02d}-{self.day:02d}"
        return birthdate
        
class AgeGenerator:
    def __init__(self):
        self.yearNow = int(datetime.datetime.now().year)

    def generate_age(self, year):
        self.age = self.yearNow - year + 1
        return self.age

class TypeGenerator:
    def __init__(self):
        self.type = None

    def load_data(self, file_path):  
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_type(self, store_file):
        self.store_data = self.load_data(store_file)
        self.type = random.choice(self.store_data)
        return f"{self.type:>6s}"

class AddressGenerator:
    def __init__(self, si_file_path, gu_file_path):
        self.si_data = self.load_data(si_file_path) # sis는 path에 있는 파일의 데이터
        self.gu_data = self.load_data(gu_file_path)
        self.si = None
        self.gu = None
        self.street = None
        self.logil = None
        self.last_num = None

    def load_data(self, file_path):  # 로드 데이터 함수는 fil_path에 있는 파일을 읽어 data에 담아 반환 하는 함수
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_address(self):
        index = random.randint(0, len(self.si_data)-1)
        self.si = self.si_data[index]
        self.gu = random.choice(self.gu_data[index].split(' '))
        self.street = str(random.randint(1,99))
        self.lo_gil = random.choice(['로','길'])
        self.last_num = str(random.randint(1,99))
        return f"{self.si:>4s} {self.gu:>4s} {self.street:>2s}{self.lo_gil} {self.last_num:>2s}"
    
class DataGenerator:
    def __init__(self, sung_file, irum_file, storeNames_file, si_file, gu_file, count):   # 객체 생성
        self.userid = None
        self.username = None
        self.userbirthday = None
        self.usergender = None
        self.userage = None
        self.useraddress = None
        self.storeid = None
        self.storename = None
        self.storeaddress = None
        self.storetype = None
        self.data = None

        while True:
            x = input("어떤 정보를 생성하시겠습니까?(user / store): ")
            if x == "user":
                self.initialSetting_user(si_file, gu_file)
                self.data = self.generate_userdata(sung_file, irum_file, count)
                break
                
            elif x == "store":
                self.initialSetting_store(si_file, gu_file)
                self.data = self.generate_storedata(storeNames_file, count)
                break

            else:
                print("다시 입력해주세요: ")

    def initialSetting_user(self, si_file, gu_file):
        self.userid_gen = IDGenerator()
        self.username_gen = NameGenerator()
        self.userbirthday_gen = BirthdateGenerator()
        self.usergender_gen = GenderGenerator()
        self.userage_gen = AgeGenerator()
        self.useraddress_gen = AddressGenerator(si_file, gu_file)

    def initialSetting_store(self, si_file, gu_file):
        self.storeid_gen = IDGenerator()
        self.storename_gen = NameGenerator()
        self.storetype_gen = TypeGenerator()
        self.storeaddress_gen = AddressGenerator(si_file, gu_file)

    def generate_userdata(self, sung_file, irum_file, count):
        userdata = []
        for _ in range(count):
            userid = self.userid_gen.generate_userid()
            username = self.username_gen.generate_username(sung_file, irum_file)
            userbirthday = self.userbirthday_gen.generate_birthdate()
            usergender = self.usergender_gen.generate_gender()
            userage = self.userage_gen.generate_age(self.userbirthday_gen.year)
            useraddress = self.useraddress_gen.generate_address()
            userdata.append((userid, username, userbirthday, usergender, userage, useraddress))
        return userdata

    def generate_storedata(self, storeNames_file, count):
        storedata = []
        for _ in range(count):
            storeid = self.storeid_gen.generate_userid()
            storetype = self.storetype_gen.generate_type(storeNames_file)
            storeaddress = self.storeaddress_gen.generate_address()
            storename = self.storename_gen.generate_storename(self.storetype_gen.type, self.storeaddress_gen.gu)
            storedata.append((storeid, storename, storetype, storeaddress))
        return storedata
    
class DataPrinter:
    def __init__(self, data, filename):  # 객체 생성
        self.x = None
        self.print_or_csv = None
        while True:
            self.x = input("어떤 정보를 출력하시겠습니까?(User / Store): ").lower()
            
            if self.x == "user":
                while True:
                    self.print_or_csv = input("Console or CSV?: ").lower()
                    if self.print_or_csv == 'console':
                        return self.userdata_export_to_console(data)
                    elif self.print_or_csv == 'csv':
                        return self.userdata_export_to_csv(data, filename)
                    else:
                        print("다시 입력해주세요.", end="")
                    
            elif self.x == "store":
                while True:
                    self.print_or_csv = input("Console or CSV?: ").lower()
                    
                    if self.print_or_csv == 'console':
                        return self.storedata_export_to_console(data)
                    elif self.print_or_csv == 'csv':
                        return self.storedata_export_to_csv(data, filename)
                    else:
                        print("다시 입력해주세요. ", end="")
# TODO: 
    def userdata_export_to_console(self, data):
        for id, name, birthdate, gender, age, address in data:
            print(f"ID:{id}\nName:{name}\nBirthdate:{birthdate}\nGender:{gender}\nAge:{age}\nAddress:{address}\n")
    
    def userdata_export_to_csv(self, data, filename):
        headers = ['ID', 'Name', 'Birthdate', 'Gender', 'Age', 'Address']
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(headers)
            wr.writerows(data)

    def storedata_export_to_console(self, data):
        for id, name, type, address in data:
            print(f"ID:{id}\nName:{name}\nType:{type}\nAddress:{address}\n")
    
    def storedata_export_to_csv(self, data, filename):
        headers = ['ID', 'Name', 'Type', 'Address']
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(headers)
            wr.writerows(data)

count_input         = int(input("몇 개의 데이터를 생성하시겠습니까?: "))
sung_file           = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/src/koreanNames_sung.txt'
irum_file           = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/src/koreanNames_irum.txt'
storeName_file      = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/src/storeNames.txt'
city_file           = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/src/koreaCities.txt'
si_file             = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/src/korea_sis.txt'
gu_file             = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/src/korea_gus.txt'
export_csv_filename = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/csv/data2.csv'

data = DataGenerator(sung_file, irum_file, storeName_file, si_file, gu_file, count_input).data
DataPrinter(data, export_csv_filename)