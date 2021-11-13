a = int(input())
b = int(input())
for i in range(a, b):
    if i == 1:
        continue
    f = 1
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            f += j + i // j
    if f == i:
        print(i)
