t = int(input())
ips = {}
for i in range(t):
    ip = input().split()[0]
    ips[ip] = ips.setdefault(ip, 0) + 1

ans, cnt = 0, 0
for i in ips:
    if ips[i] > cnt:
        ans = i
        cnt = ips[i]
print(ans, cnt)
