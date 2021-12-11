n, m = map(int, input().split())

a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

maxn = 0
minn = 1e9
kmaxx = kmaxy = kminx = kminy = -1
for i in range(n):
    for j in range(m):
        if a[i][j] > maxn:
            maxn = a[i][j]
            kmaxx = i + 1
            kmaxy = j + 1
        elif a[i][j] < minn:
            minn = a[i][j]
            kminx = i + 1
            kminy = j + 1

print(kmaxx, kmaxy, a[kmaxx - 1][kmaxy - 1])
print(kminx, kminy, a[kminx - 1][kminy - 1])
