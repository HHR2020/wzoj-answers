n = int(input())
s = 0
p, q = 1, 2
for i in range(n):
    s += q / p
    q, p = q + p, q
print("%.4f" % s)
