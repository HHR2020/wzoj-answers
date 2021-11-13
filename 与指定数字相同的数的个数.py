n, m = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for a in l:
    if a == m:
        s += 1
print(s)
