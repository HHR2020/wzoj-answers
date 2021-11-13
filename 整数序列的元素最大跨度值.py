l = list(map(int, input().split()))
max, min = -1, 1000000000000
for i in l:
    if i > max:
        max = i
    elif i < min:
        min = i
print(max - min)
