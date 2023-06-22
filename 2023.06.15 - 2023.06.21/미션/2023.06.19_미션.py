# 숙제
users = [
    {"name": "Alice",   "age": 25,  "location": "Seoul",  "car": "BMW"},
    {"name": "Bob",     "age": 30,  "location": "Busan",  "car": "Mercedes"},
    {"name": "Charlie", "age": 35,  "location": "Daegu",  "car": "Audi"}]

def find_users3(search_user):
    l = len(search_user.keys()) # 키의 개수 (4)
    for user in users:
        count = 0
        for p_key in search_user.keys():
            if user[p_key] == search_user[p_key]: # 키 값이 올바르면 count += 1
                count += 1
            if count == l:  # 입력으로 주어진 모든 키들의 값이 올바르면
                return user
    return "리스트에 존재하지 않습니다."

search_user1={"name": "Alice",
              "age": 25}
print(find_users3(search_user1))
search_user2={"name": "Alice",
              "age": 20,
              }
print(find_users3(search_user2))