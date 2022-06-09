n = 10
s = input()
# 开始游戏
a = [0] * (n + 1)
for c in s:
    t = int(c)
    for i in range(n - 2, -1, -1):  # i == 0时候方块可以直接到达底部
        if a[i] // 2**t % 2 == 1 or a[i + 1] // 2 ** (t - 1) % 2 == 1 or i == 0:
            a[i + 1] = a[i + 1] + 2**t
            a[i + 2] = a[i + 2] + 2**t + 2 ** (t - 1)
            break
for i in range(n, 0, -1):
    ans = ""
    for j in range(n):
        if a[i] % 2 == 1:
            ans = "#" + ans
        else:
            ans = " " + ans
        a[i] //= 2
    print(ans)
