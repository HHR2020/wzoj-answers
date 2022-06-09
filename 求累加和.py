s = 0
for i in range(1, 101):
    s += i
for i in range(1, 51):
    s += i**2
for i in range(1, 11):
    s += 1 / i
print("%.4f" % s)
