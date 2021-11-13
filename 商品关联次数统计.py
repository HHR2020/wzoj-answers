n, m, T = map(int, input().split())
carts = []
for i in range(m):
    carts.append(list(map((lambda s: int(s[1:])), input().split(","))))
for i in range(T):
    x, y = map(int, input().split())
    times = 0
    for j in carts:
        if x in j and y in j:
            times += 1
    print(times)
