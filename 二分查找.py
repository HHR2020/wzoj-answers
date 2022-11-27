n = int(input())
seq = [1] + [int(i) for i in input().split()]
x = int(input())
l, r = 1, n
times = 1
while l <= r:
    mid = (l + r) // 2
    if seq[mid] == x:
        print(mid, times)
        break
    elif seq[mid] > x:
        r = mid - 1
    else:
        l = mid + 1
    times += 1
