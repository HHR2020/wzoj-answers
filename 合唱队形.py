n = int(input())
l = list(map(int, input().split()))
l = [0] + l
highest = l.index(max(l))
for i in range(highest, n):
    if l[i] <= l[i + 1]:
        print("NoAnsweR!")
        exit()
for i in range(1, highest):
    if l[i] >= l[i + 1]:
        print("NoAnsweR!")
        exit()
print(highest)
