h1,h2=map(int,input().split())
a=input().split()
count=0
for h in a:
    x=int(h)
    if h2<x<h1:
        count += 1
if count > 0:
    print(count)
else:
    print("-1")