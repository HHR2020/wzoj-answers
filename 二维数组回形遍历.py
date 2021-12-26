def up(a: list):
    empty(a)
    print(*a.pop(0), sep="\n")
    right(a)


def right(a: list):
    empty(a)
    print(*[row.pop() for row in a], sep="\n")
    down(a)


def down(a: list):
    empty(a)
    print(*a.pop()[::-1], sep="\n")
    left(a)


def left(a: list):
    empty(a)
    print(*[row.pop(0) for row in a][::-1], sep="\n")
    up(a)


def empty(a: list):
    if a == [] or a[0] == []:
        exit()


row, col = map(int, input().split())
array = []
for i in range(row):
    array.append(input().split())

up(array)
