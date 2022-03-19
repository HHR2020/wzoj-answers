p = 998244353


def power(c, b, e):
    if e == 0:
        return c % p
    elif e % 2 == 0:
        return power(c, b * b % p, e // 2)
    else:
        return power(c * b % p, b, e - 1)


print(power(1, 2, int(input())))
