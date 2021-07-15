k=int(input())
a,b=0,1
for i in range(k):
    a,b=b,a+b
    if i==k-1:
        print(a)