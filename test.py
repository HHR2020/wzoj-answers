n=int(input())
cnt=0
for i in range(0,n+1,3):
    for j in range(0,n-i+1):
        if i/3+j*5+(n-i-j)*3==n:
            cnt+=1
print(cnt)