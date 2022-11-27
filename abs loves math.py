from math import gcd
import sys

sys.setrecursionlimit = 100000000000


def fib(n):
    def fib_iter(a, b, p, q, n):
        if n == 0:
            return b
        elif n % 2 == 0:
            return fib_iter(a, b, p * p + q * q, 2 * p * q + q * q, n // 2)
        else:
            return fib_iter(b * q + a * q + a * p, b * p + a * q, p, q, n - 1)

    return fib_iter(1, 0, 0, 1, n)


n = int(input())
a = [fib(int(input())) for i in range(n)]
print(gcd(*a))
