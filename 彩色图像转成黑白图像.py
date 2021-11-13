n, m = map(int, input().split())
photo = [[None for i in range(m)] for j in range(n)]
for i in range(n):
    s = [int(c) for c in input().split(",")]
    for j in range(m):
        photo[i][j] = int(
            s[j * 3] * 0.299 + s[j * 3 + 1] * 0.587 + s[j * 3 + 2] * 0.114 < 132
        )
        print(photo[i][j], end="")
    print()
t = int(input())
for i in range(t):
    x, y = map((lambda x: int(x) - 1), input().split())
    print(photo[x][y])
