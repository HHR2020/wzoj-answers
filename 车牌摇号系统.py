n = int(input())
l = [input() for i in range(n)]
m = int(input())
ans = []
for i in range(m):
    c = int(input()) - 1
    if not l[c] in ans:
        ans.append(l[c])
    else:
        m -= 1
print(*ans, sep="\n")
print(m)
