import csv

headers = ['ID', 'Name', 'Type', 'Address']
with open("excel.csv", 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(headers)
    wr.writerows(("138ㅐ714", "오소현", "여자", "봉화산"))