n = int(input())
m = 2 * n - 1
a = [[0 for j in range(m + 1)] for i in range(m + 1)]
x, y = 1, n
a[x][y] = 1
for i in range(2, m * m + 1):
    nx = x - 1
    ny = y + 1
    if nx == 0:
        nx = m
    if ny == m + 1:
        ny = 1
    if a[nx][ny] != 0:
        nx = x + 1
        ny = y
    a[nx][ny] = i
    x, y = nx, ny
for i in range(1, m + 1):
    for j in range(1, m + 1):
        print(a[i][j], end=" ")
    print()
