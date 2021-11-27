x = int(input())
if x >= 0:  # 正数的反码、补码与原码相同
    ans = ""
    for i in range(8):
        ans = str(x % 2) + ans
        x //= 2
    print(ans)
    print(ans)
else:
    x = -x
    a = [0] * 7
    ans = ""
    for i in range(7):
        a[i] = 1 - x % 2
        x = x // 2
        ans = str(a[i]) + ans
    ans = "1" + ans
    print(ans)  # 输出反码

    ans = ""
    i = 0
    a[0] = a[0] + 1
    while a[i] == 2:
        a[i] = 0
        a[i + 1] += 1
        i = i + 1
    ans = "1"
    for i in range(7):
        ans = ans + str(a[6 - i])
    print(ans)  # 输出补码
