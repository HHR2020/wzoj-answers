n=int(input())
l=list(map(int,input().split()))
m=l[0]
index=0
for i in range(1,n):
    if l[i]<m:
        m=l[i]
        index=i
l[0],l[index]=l[index],l[0]
for i in l:
    print(i,end=" ")