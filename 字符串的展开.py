p1, p2, p3 = map(int, input().split())
s = input().split("-")
for i in range(0, len(s) - 1):
    print(s[i], end="")
    left = s[i][-1:-2:-1]
    right = s[i + 1][0:1]
    if not (
        (
            (left.islower() and right.islower())
            or (left.isnumeric() and right.isnumeric())
        )
        and left < right
    ):
        print("-", end="")
        continue
    else:
        filling = ""
        for i in range(ord(left) + 1, ord(right)):
            filling += chr(i) * p2
        if p3 == 2:
            filling = filling[::-1]
        if (left + right).islower() and p1 == 2:
            filling = filling.upper()
        if p1 == 3:
            filling = "*" * len(filling)
    print(filling, end="")
print(s[-1])
