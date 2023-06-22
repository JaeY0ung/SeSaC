even_numbers = [x for x in range(1,21) if x%2==0]
print(even_numbers)


# 1
word = "hello"
upper_letters = list(word.upper())
print(upper_letters)
# 2
upper_letters = []
for i in word:
    upper_letters.append(i.upper())
print(upper_letters)
#3
upper_letters=[x.upper() for x in word]
print(upper_letters)

words = ["apple", "banana", "cherry", "dragonfruit", "egg"]
short_words = [word for word in words if len(word)<=3]
print(short_words)

users = [
    {"name": "Alice",   "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob",     "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]
#1
def find_users1(name):
    for dic in users:
        if dic["name"] == name:
            return dic
    return "리스트에 없습니당"
print(find_users1("Alice"))

#2
def find_users2(name, age):
    for dic in users:
        if dic["name"] == name and dic["age"] == age:
            return dic
    return "리스트에 존재하지 않습니다."

print(find_users2("Alice", 25))
print(find_users2("Alice", 30))
print()
# 맥스 값 찾기
numbers=[1,2,33,4,5,6,67,78,8,4,4,45,6,7,78,8]
def find_max(arr):
    if len(arr) == 0:
        return None
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max
print(find_max(numbers))
print(find_max([]))


# Name,Birthdate,Gender,Address
# Jane,1990-01-03,Male,50 New York
# Jane,1990-04-14,Male,46 Philadelphia
# Jane,1981-01-07,Male,69 Los Angeles
# Emily,1975-09-03,Female,33 Philadelphia
# Olivia,1987-12-18,Male,2 Chicago
# Michael,1980-03-21,Male,18 Chicago
# Michael,1982-03-02,Male,57 Houston
# Olivia,1976-10-19,Female,36 Chicago
# Emily,1976-01-05,Female,96 New York
# John,1971-08-22,Male,76 Los Angeles
# Jane,1984-11-26,Male,7 Houston

#1
numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
def remove_duplicate(arr):
    unique_list = []
    for i in arr:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
unique_list = remove_duplicate(numbers)

#2
numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
def remove_duplicate(arr):
    return list(set(arr))

print("원본리스트: ", numbers)
print("유닉리스트: ", unique_list)


# 3
import sys
numbers = sys.stdin.readline().split()
arr = [int(i) for i in numbers]
print(find_max(arr))

#4
import sys
arr = list(map(int, sys.stdin.readline().split()))
print(find_max(arr))
