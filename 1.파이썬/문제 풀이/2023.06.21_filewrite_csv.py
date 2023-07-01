# csv = comma separated value
import csv

data = [
    ('name',"age","city"),
    ("John",25,"seoul")
]
with open("user.csv", "w",newline="") as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)