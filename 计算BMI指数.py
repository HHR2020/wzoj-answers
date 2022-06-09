m, h = map(float, input().split())
bmi = m / (h**2)
if bmi < 18.5:
    print("thin!")
elif bmi <= 25:
    print("normal!")
else:
    print("fat!")
