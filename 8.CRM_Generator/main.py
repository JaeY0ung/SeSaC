import random
import csv 
import uuid
import datetime


sung_file          = './src/koreanNames_sung.txt'
irum_file          = './src/koreanNames_irum.txt'
storetype_file     = './src/store_types.txt'
si_file            = './src/korea_sis.txt'
gu_file            = './src/korea_gus.txt'

user_csvfile      = './csv/crm_user.csv'
store_csvfile     = './csv/crm_store.csv'
order_csvfile     = './csv/crm_order.csv'
orderitem_csvfile = './csv/crm_orderitem.csv'
item_csvfile      = './csv/crm_item.csv'

# 인자 : X
class IDGenerator:
    def generate_id(self):
        id = uuid.uuid4()
        return id
    
# 인자 : sung_file, irum_file
class UserNameGenerator:
    # 파일 로드는 한번만 실행시키기 위해
    def __init__(self, sung_file, irum_file):
        self.sung_data = self.read_file(sung_file)
        self.irum_data = self.read_file(irum_file)

    def read_file(self, file):
        with open(file, "r") as file:
            data = file.read().splitlines()  # 여러줄을 가져와서 line으로 쪼개기
        return data
    
    def generate_username(self):
        sung = random.choice(self.sung_data)
        irum = random.choice(self.irum_data)
        fullname = f"{sung}{irum}"
        return fullname

# 인자 : X
class UserGenderGenerator:
    def generate_gender(self):
        usergender = random.choice(["Male", "Female"])
        return f"{usergender:>6s}"

# 인자 : birthyear (태어난 년도)      
class AgeGenerator:
    def generate_age(self, birthyear):
        age = int(datetime.datetime.now().year) - int(birthyear) + 1
        return age

# 인자 : X
class UserBirthdateGenerator:
    def generate_birthdate(self):
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        year = random.randint(1960, 2022)
        month = random.randint(1,12)
        day = random.randint(1, month_days[month-1] + 1)
        birthdate = f"{year}-{month:02d}-{day:02d}"
        return birthdate

# 인자 : shop_type ( ex. 투썸,이디야 ), shop_address_gu ( ex. 동대문구 )
class StoreNameGenerator:
    def generate_storename(self, shop_type, shop_address_gu):
        ho = random.randint(1, 9)
        storename = f"{shop_type:>6s} {shop_address_gu:>4s}{ho}호점"
        return storename

# 인자 : storeName_file
class StoreTypeGenerator:
    def __init__(self, storetype_file):
        self.store_data = self.read_file(storetype_file)
        self.type = None

    def read_file(self, file_path):  
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_type(self):
        self.type = random.choice(self.store_data)
        return f"{self.type:>6s}"

# 인자 : X
class OrderAtGenerator:
    def generate_orderat(self):
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        month = random.randint(1, 12)
        day = random.randint(1, month_days[month-1] + 1)
        hour = random.randint(0,24)
        miniute = random.randint(0,60)
        second = random.randint(0,60)
        orderat = f"2023-{month:02d}-{day:02d} {hour:02d}:{miniute:02d}:{second:02d}"
        return orderat

# 인자 : user_csvfile, store_csvfile
class User_StoreIdGenerator_in_Order:
    def __init__(self, user_csvfile, store_csvfile):
        self.userid_data= self.read_csv(user_csvfile)
        self.storeid_data= self.read_csv(store_csvfile)
        
    def read_csv(self, csvfile):  # 로드 데이터 함수는 fil_path에 있는 파일을 읽어 data에 담아 반환 하는 함수
        data = []
        with open(csvfile, 'r', encoding= 'UTF-8') as file:
            csvReader = csv.DictReader(file)
            for row in csvReader:
                data.append(row['Id'])
        return data

    def generate_user_id(self):
        userid = random.choice(self.userid_data)
        return userid
    
    def generate_store_id(self):
        storeid = random.choice(self.storeid_data)
        return storeid

class Order_ItemIdGenerator_in_Orderitems:
    def __init__(self, order_csvfile, item_csvfile):
        self.orderid_data= self.read_csv(order_csvfile)
        self.itemid_data= self.read_csv(item_csvfile)
        
    def read_csv(self, csvfile):  # 로드 데이터 함수는 fil_path에 있는 파일을 읽어 data에 담아 반환 하는 함수
        data = []
        with open(csvfile, 'r', encoding= 'UTF-8') as file:
            csvReader = csv.DictReader(file)
            for row in csvReader:
                data.append(row['Id'])
        return data

    def generate_order_id(self):
        orderid = random.choice(self.orderid_data)
        return orderid
    
    def generate_item_id(self):
        itemid = random.choice(self.itemid_data)
        return itemid

# 인자 : X
class ItemNameGenerator:
    def __init__(self):
        self.item_type = None
        self.item_price = None
        self.item_types = {
            "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }

    def generate_itemname(self):
        item_type = random.choice(list(self.item_types.keys()))
        item_type_detail = random.choice(list(self.item_types[item_type]))
        item_price = self.item_types[item_type][item_type_detail]
        self.item_type = item_type
        self.item_price = item_price
        return f"{item_type_detail} {item_type}"
    
    def generate_itemtype(self):
        return f"{self.item_type}"
    
    def generate_itemprice(self):
        return self.item_price
# 인자 : si_file, gu_file
class AddressGenerator:
    # 파일 로드는 한번만 실행시키기 위해
    def __init__(self, si_file, gu_file):
        self.si_data = self.read_file(si_file)
        self.gu_data = self.read_file(gu_file)
        self.gu = None

    def read_file(self, file_path): 
        with open(file_path, "r") as file:
            data = file.read().splitlines()
        return data
    
    def generate_address(self):
        index = random.randint(0, len(self.si_data)-1)
        si = self.si_data[index]
        gu = random.choice(self.gu_data[index].split(' '))
        street = random.randint(1,99)
        lo_gil = random.choice(['로','길'])
        last_num = random.randint(1,99)
        self.gu = gu
        return f"{si} {gu} {street:02d}{lo_gil} {last_num:02d}"

##################
# DATA GENERAGOR #
##################
class UserDataGenerator:
    def __init__(self, sung_file, irum_file, si_file, gu_file):
        self.id_gen = IDGenerator()
        self.username_gen = UserNameGenerator(sung_file, irum_file)
        self.birthdate_gen = UserBirthdateGenerator()
        self.gender_gen = UserGenderGenerator()
        self.age_gen = AgeGenerator()
        self.address_gen = AddressGenerator(si_file, gu_file)
        self.userheader = []

    def generate_user(self, count):
        data = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            name = self.username_gen.generate_username()
            birthdate = self.birthdate_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            age = self.age_gen.generate_age(birthdate[:4])
            address = self.address_gen.generate_address()
            
            keys = ['Id', 'Name', 'Birthdate', 'Gender', 'Age', 'Address']
            values = [id, name, birthdate, gender, age, address]
            self.userheader = keys
            data.append(dict(zip(keys, values)))
        return data

class StoreDataGenerator:
    def  __init__(self, storetype_file, si_file, gu_file):
        self.id_gen = IDGenerator()
        self.storename_gen = StoreNameGenerator()
        self.type_gen = StoreTypeGenerator(storetype_file)
        self.address_gen = AddressGenerator(si_file, gu_file)
        self.storeheader = []
    
    def generate_store(self, count):
        data = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            type = self.type_gen.generate_type()
            address = self.address_gen.generate_address()
            name = self.storename_gen.generate_storename(self.type_gen.type, self.address_gen.gu)

            keys = ['Id', 'Name', 'Type', 'Address']
            values = [id, name, type, address]
            self.storeheader = keys
            data.append(dict(zip(keys, values)))
        return data
    
class OrderDataGenerator:
    def  __init__(self, user_csvfile, store_csvfile):
        self.id_gen = IDGenerator()
        self.orderat_gen = OrderAtGenerator()
        self.user_store_gen = User_StoreIdGenerator_in_Order(user_csvfile, store_csvfile)
        self.orderheader = []
    
    def generate_order(self, count):
        data = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            orderat = self.orderat_gen.generate_orderat()
            storeid = self.user_store_gen.generate_store_id()
            userid =  self.user_store_gen.generate_user_id()

            keys = ['Id', 'OrderAt', 'StoreId', 'UserId']
            values = [id, orderat, storeid, userid]
            self.orderheader = keys
            data.append(dict(zip(keys, values)))
        return data
    
class OrderItemDataGenerator:
    def  __init__(self, order_csvfile, item_csvfile):
        self.id_gen = IDGenerator()
        self.order_item_gen = Order_ItemIdGenerator_in_Orderitems(order_csvfile, item_csvfile)
        self.orderitemheader = []
    
    def generate_orderitem(self, count):
        data = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            orderid = self.order_item_gen.generate_order_id()
            itemid = self.order_item_gen.generate_item_id()

            keys = ['Id', 'OrderId', 'ItemId']
            values = [id, orderid, itemid]
            self.orderitemheader = keys
            data.append(dict(zip(keys, values)))
        return data
    
class ItemDataGenerator:
    def  __init__(self):
        self.id_gen = IDGenerator()
        self.name_type_unitprice_gen = ItemNameGenerator()
        self.itemheader = []
    
    def generate_item(self, count):
        data = []
        for _ in range(count):
            id = self.id_gen.generate_id()
            name = self.name_type_unitprice_gen.generate_itemname()
            type = self.name_type_unitprice_gen.generate_itemtype()
            unitprice = self.name_type_unitprice_gen.generate_itemprice()

            keys = ['Id', 'Name', 'Type', 'UnitPrice']
            values = [id, name, type, unitprice]
            self.itemheader = keys
            data.append(dict(zip(keys, values)))
        return data

class CSV_Printer:    
    def data_export_to_csv(self, data, csv_file, header):
        with open(csv_file, 'w', newline='') as file:
            csvWriter = csv.DictWriter(file, header)
            csvWriter.writeheader()
            csvWriter.writerows(data)


csv_printer = CSV_Printer()

data_gen = UserDataGenerator(sung_file, irum_file, si_file, gu_file)
userdata = data_gen.generate_user(1000)
csv_printer.data_export_to_csv(userdata, user_csvfile, data_gen.userheader)


data_gen = StoreDataGenerator(storetype_file, si_file, gu_file)
storedata = data_gen.generate_store(500)
csv_printer.data_export_to_csv(storedata, store_csvfile, data_gen.storeheader)

data_gen = OrderDataGenerator(user_csvfile, store_csvfile)
orderdata = data_gen.generate_order(10000)
csv_printer.data_export_to_csv(orderdata, order_csvfile, data_gen.orderheader)

data_gen = ItemDataGenerator()
itemdata = data_gen.generate_item(15)
csv_printer.data_export_to_csv(itemdata, item_csvfile, data_gen.itemheader)

data_gen = OrderItemDataGenerator(order_csvfile, item_csvfile)
orderitemdata = data_gen.generate_orderitem(10000)
csv_printer.data_export_to_csv(orderitemdata, orderitem_csvfile, data_gen.orderitemheader)
