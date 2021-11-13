num = int(input())
a = num % 10
b = num // 10 % 10
c = num // 100
if c < b:
    c, b = b, c
if c < a:
    c, a = a, c
if b < a:
    b, a = a, b
max = 100 * c + 10 * b + a
min = 100 * a + 10 * b + c
print(max)
print(min)
