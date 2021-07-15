s=input().split()
a=input()
b=input()
for item in s:
    if a==item:
        print(b,end=" ")
    else:
        print(item,end=" ")