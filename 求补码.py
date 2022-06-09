s = input()
sign = int(s[0])
if sign == 0:
    print(s)
else:
    n = (2**15 - 1) ^ int(s[1:], 2)
    print("{:0>16b}".format((n + (sign << 15) + 1) % 2**16))
