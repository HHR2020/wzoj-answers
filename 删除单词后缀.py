a=input()
if a[len(a)-2:]=="er" or a[len(a)-2:]=="ly":
    print(a[:len(a)-2])
elif a[len(a)-3:]=="ing":
    print(a[:len(a)-3])
else:
    print(a)
