def h(a, b, c, n, no):
    global s
    if n == 1:
        s += f"{no} from {a} to {c}\n"
        return 1
    else:
        return h(a, c, b, n - 1, 1) + h(a, b, c, 1, n) + h(b, a, c, n - 1, 1)


s = "\n"
n = int(input())
print(h("A", "B", "C", n, n), s)
