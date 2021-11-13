n = int(input())
l = list(map(int, input().split()))
a, b = map(int, input().split())
l.insert(a, b)
for i in l:
    print(i, end=" ")
