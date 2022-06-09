n, k, a = map(int, input().split())


def age(n, k, a):
    if n == 1:
        return a
    else:
        return k + age(n - 1, k, a)


print(age(n, k, a))
