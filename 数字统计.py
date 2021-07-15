L,R=map(int,input().split())
s=0
for i in range(L,R+1):
    for j in str(i):
        if j=='2':
            s+=1
print(s)