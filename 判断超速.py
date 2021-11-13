s = float(input())
t = float(input())
t = t / 3600
v = s / t
if v <= 100:
    print("no")
elif v < 120:
    print("yes")
    print("%.2f" % v)
elif v < 150:
    print("yes")
    print("%.2f" % v)
elif v < 170:
    print("yes")
    print("%.2f" % v)
else:
    print("yes")
    print("%.2f" % v)
