from random import random
import math

score = 0
m = "98652"
print("\t横坐标\t纵坐标\t距离\t得分")
for i in range(1, 11):
    x = int((random() * 201 - 100)) / 10
    y = int((random() * 201 - 100)) / 10
    r = round(math.sqrt(x ** 2 + y ** 2), 1)
    h = int(r)
    s = 0
    if h < 10:
        s = int(m[h // 2])
    print(i, "\t", x, "\t", y, "\t", r, "\t", s)
    score = score + s
print("总得分", score)
