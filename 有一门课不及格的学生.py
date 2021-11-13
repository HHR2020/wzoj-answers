a, b = map(float, input().split())
if a < 60 and b >= 60 or b < 60 and a >= 60:
    print("1")
else:
    print("0")
