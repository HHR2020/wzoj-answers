a, b, c = map(int, input().split())
x1 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
if x1 < x2:
    x1, x2 = x2, x1
print("%.2f" % x1, "%.2f" % x2)
