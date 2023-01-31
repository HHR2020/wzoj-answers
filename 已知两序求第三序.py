pre = input()
mid = input()


def iter(p, m):
    if not p:
        return
    i = m.find(p[0])
    iter(p[1 : i + 1], m[:i])
    iter(p[i + 1 :], m[i + 1 :])
    print(p[0], end="")


iter(pre, mid)
