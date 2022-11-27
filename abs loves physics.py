n = int(input())
mx = my = mz = M = 0
for i in range(n):
    x, y, z, m = map(int, input().split())
    mx += m * x
    my += m * y
    mz += m * z
    M += m
print(mx // M)
print(my // M)
print(mz // M)
