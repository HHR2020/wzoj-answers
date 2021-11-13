a, b, c = map(float, input().split())
if a + b <= c or b + c <= a or c + a <= b:
    print("Can't")
else:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("%.2f" % s)
