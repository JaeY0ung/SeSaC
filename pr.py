import random

arr = [i for i in range(1,11)]
for i in range(10):
    num = random.choice(arr)
    input()
    print(num)
    arr.remove(num)
    