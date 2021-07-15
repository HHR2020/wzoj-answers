m,k=input().split()
k=int(k)
cnt=0
for item in m:
    if item=='3':
        cnt+=1
if int(m)%19==0 and cnt==k:
    print("YES")
else:
    print("NO")