x = int(input())

ans = ""
while x > 0:
    a = x % 10
    a1 = a // 5
    a = a % 5
    a2 = a // 4
    a = a % 4
    a3 = a // 2
    a = a % 2
    x = x // 10
    ans = "{}{}{}{}".format(a1, a2, a3, a) + ans

print(ans)
