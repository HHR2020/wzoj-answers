n=int(input())
m=0
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    if 90<=a<=140 and 60<=b<=90:
        cnt+=1
        continue
    elif cnt>m:
        m=cnt
    cnt=0
if cnt>m:
    m=cnt
print(m)