n = int(input())
a = [input().split() for i in range(n)]
b = [input().split() for i in range(n)]
flag1 = flag2 = flag3 = flag4 = True
for i in range(n):
    for j in range(n):
        if a[i][j] != b[j][n - i - 1]:
            flag1 = False
for i in range(n):
    for j in range(n):
        if a[i][j] != b[n - j - 1][i]:
            flag2 = False
for i in range(n):
    for j in range(n):
        if a[i][j] != b[n - i - 1][n - j - 1]:
            flag3 = False
if a != b:
    flag4 = False
if flag1:
    print(1)
elif flag2:
    print(2)
elif flag3:
    print(3)
elif flag4:
    print(4)
else:
    print(5)
