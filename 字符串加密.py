def btoh(b):
    # 自定义函数是将b中存储的二进制反码转换成对应的十六进制数
    h = 0
    H = ""
    for i in range(8):
        h = h * 2 + int(b[i])
        if (i + 1) % 4 == 0:
            if 0 <= h <= 9:
                H = H + str(h)
            else:
                H = H + chr(ord("A") + h - 10)
            h = 0
    return H


s = input()
mw = ""
for i in s:
    m = ord(i)
    b = ""
    for j in range(8):
        r = 1 - m % 2
        m = m // 2
        b = str(r) + b
    mw = btoh(b) + mw
print(mw)
