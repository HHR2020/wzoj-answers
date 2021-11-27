x = input().strip()  # strip()函数是去除行末的空格与回车符
y = input().strip()
dis = len(x) - len(y)
if dis < 0:
    x, y = y, x
    dis = -dis
for i in range(dis):
    y = "0" + y
jw = 0
ans = ""
for i in range(len(x) - 1, -1, -1):
    a = int(x[i]) + int(y[i]) + jw
    jw = a // 2
    ans = str(a % 2) + ans
if jw == 1:
    ans = "1" + ans
print(ans)

"""
a = int(input(), 2)
b = int(input(), 2)
print("{:b}".format(a + b))
"""
