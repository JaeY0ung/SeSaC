# 2022.12.31 = 2023.01.00 = 토요일   / 일=0 월=1 화=2 수=3 목= 4금=5 토=6
# 2016.12.31 = 2017.01.00 = 0001.01.00 일요일

common_year = {
    "days":365,
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
specific_year = {
    "days":366,
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
year = int(input("연도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
weekarr = ['일','월','화','수','목','금','토']
sum = 0
for y in range(0, year):
    if y%100 == 0 and y%400 != 0:
        sum += 365
    elif y%4 == 0 or y%400 == 0:
        sum += 366
if year%100 == 0 and year%400 != 0:
        for m in range(1,month):
            sum += common_year[m]
elif year%4 == 0 or year%400 == 0:
     for m in range(1,month):
            sum += specific_year[m]
print(weekarr[sum%7])
    
