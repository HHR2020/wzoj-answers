n = int(input())
a = [[0 for j in range(i + 1)] for i in range(n)]
for i in range(0, n):
    a[i][0] = a[i][i] = 1
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
for i in range(n):
    print(a[i])
