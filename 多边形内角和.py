n = int(input())
x = 180 * (n - 2)
angle = input().split()
for i in angle:
    x -= int(i)
print(x)
