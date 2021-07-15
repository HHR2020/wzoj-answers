n,x,y=map(int,input().split())
left=int(n-y/x)
if left >= 0:
    print(left)
else:
    print("0")