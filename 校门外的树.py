L, M = map(int, input().split())
road = [1] * (L + 1)
for _i in range(M):
    l, r = map(int, input().split())
    for index in range(l, r + 1):
        road[index] = 0
print(sum(road))
