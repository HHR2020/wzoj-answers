n,m=map(int,input().split())
l=[0]*(n+1)
for i in range(1,n+1):
    l[i]=int(input())
for i in range(m):
    x=int(input())
    print(max(l[:x+1]))