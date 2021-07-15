number=list(map(int,input().split()))
cp,cn,sp,sn=0,0,0,0
for i in number:
    if i>0:
        cp+=1
        sp+=i
    elif i<0:
        cn+=1
        sn+=i
print(cp,cn,sp,sn)