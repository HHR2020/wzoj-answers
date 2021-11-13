point = input().split(",")
x, y = 0, 0
d = 0
for i in range(0, len(point), 2):
    a = point[i]
    b = point[i + 1]
    a = float(a)
    b = float(b)
    d += ((a - x) ** 2 + (b - y) ** 2) ** 0.5
    x, y = a, b
print("%.5f" % d)
