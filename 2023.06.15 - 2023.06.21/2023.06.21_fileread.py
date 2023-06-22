with open("names.txt", "r") as file:
    lines = file.readlines() # 한번에 읽어오기

for line in lines:
    print(line, end='')

names = []

for line in lines: 
    names.append(line.strip())
print(names)