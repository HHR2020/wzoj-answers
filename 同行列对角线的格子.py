n, x, y = map(int, input().split())
for i in range(1, n + 1):
    print(f"({x},{i})", end=" ")
print()
for i in range(1, n + 1):
    print(f"({i},{y})", end=" ")
print()
for i in range(1, n + 1):
    j = i - x + y  # 可用直线解析式的方式思考，下同
    if 1 <= j <= n:
        print(f"({i},{j})", end=" ")
print()
for i in range(n, 0, -1):
    j = x + y - i
    if 1 <= j <= n:
        print(f"({i},{j})", end=" ")
print()
