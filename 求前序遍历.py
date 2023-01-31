mid = input()
after = input()


def iter(m, a):
    if not m:
        return
    print(a[-1], end="")
    i = m.find(a[-1])
    iter(m[:i], a[:i])
    iter(m[i + 1 :], a[i:-1])


iter(mid, after)
