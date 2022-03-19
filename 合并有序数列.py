m, n = input().split()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = []
a, b = (a, b) if a[-1] < b[-1] else (b, a)
while b != []:
    if a == []:
        r = r + b
        print(*r)
        exit()
    else:
        if a[0] < b[0]:
            r.append(a[0])
            a = a[1:]
        else:
            r.append(b[0])
            b = b[1:]
