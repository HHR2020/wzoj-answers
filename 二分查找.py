n = int(input())
seq = [1] + [int(i) for i in input().split()]
x = int(input())
left, right = 1, n
times = 1
while left <= right:
    mid = (left + right) // 2
    if seq[mid] == x:
        print(mid, times)
        break
    elif seq[mid] > x:
        right = mid - 1
    else:
        left = mid + 1
    times += 1
