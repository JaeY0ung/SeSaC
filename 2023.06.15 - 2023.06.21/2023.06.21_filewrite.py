import os

data = "Hello World\n"
filepath = " "
filename = " "
os.mkdir(filepath)

with open(filepath+filename,'a') as file:
    file.write(data)
print("파일쓰기 완료!")