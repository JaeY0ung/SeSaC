import random

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
genders = ["Male", "Female"]
birth_years = [i for i in range(1960,2023)]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
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
    return year, month, day
def generate_address():
    return random.choice(cities)

data = []

for _ in range(10):
    name = generate_name()
    birth_year  = generate_birthdate()[0]
    birth_month = generate_birthdate()[1]
    birth_day   = generate_birthdate()[2]
    birth_date =str(birth_year) + '-' + str(birth_month) + '-' + str(birth_day)
    gender = generate_gender()
    age = yearNow - birth_year + 1
    address = generate_address()
    data.append([name, birth_date, gender, age, address])

for d in data:
    print(d)