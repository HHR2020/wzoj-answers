import math

x, n = map(eval, input().split())


def f(n, x):
    if n == 1:
        return math.sqrt(x + n)
    else:
        return math.sqrt(n + f(n - 1, x))


print(f"{f(n, x):.3f}")
