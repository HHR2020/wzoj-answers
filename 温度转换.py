m = list(map(int, input().split()))
left, right = min(m), max(m)
for i in range(left, right + 1, 2):
    print(f"{i} {9*i/5+32:.1f}")
