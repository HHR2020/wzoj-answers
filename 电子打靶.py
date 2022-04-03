import math

score = 0
m = "98652"
print("  \tX\tY\tDis\tScore")
for i in range(1, 11):
    x, y = map(eval, input().split())
    r = round(math.sqrt(x**2 + y**2), 1)
    h = int(r)
    s = 0
    if h < 10:
        s = int(m[h // 2])
    print("%d.\t%0.1f\t%0.1f\t%0.1f\t%d" % (i, x, y, r, s))
    score = score + s
print("total = ", score)
