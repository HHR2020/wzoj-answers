a, b = map(int, input().split())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/" and b != 0:
    print(a // b)
else:
    print("Error!")
