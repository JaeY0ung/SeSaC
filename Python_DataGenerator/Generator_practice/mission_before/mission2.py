import random
import csv 

# names.txt 파일 읽어오기
names = []
with open("names.txt","r") as file:
    lines = file.readlines()
for line in lines: 
    names.append(line.strip())

genders = ["Male", "Female"]
birth_years = [i for i in range(1960, 2023)]

# cities.txt 파일 읽어오기
cities = []
with open("cities.txt","r") as file:
    lines = file.readlines()
for line in lines: 
    cities.append(line.strip())
month_days = [0,31,30,31,30,31,30,31,31,30,31,30,31]
yearNow = 2023

def generate_name():
    return random.choice(names)

def generate_gender():
    return random.choice(genders)

def generate_birthdate():
    year = random.choice(birth_years)
    month = random.choice([_ for _ in range(1,13)])
    day = random.choice([_ for _ in range(1, month_days[month]+1)])
    age =  yearNow - year + 1
    return f"{year}", f"{month:02d}", f"{day:02d}", f"{age:02d}"

def generate_address():
    return random.choice(cities)

data = []
for _ in range(10):
    name = generate_name()
    birth_date = generate_birthdate()[0] + '-' + generate_birthdate()[1] + '-' + generate_birthdate()[2]
    gender = generate_gender()
    age = str(generate_birthdate()[3])
    address = generate_address()
    data.append([name, birth_date, gender, age, address])
print(data)