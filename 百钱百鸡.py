import math
n=int(input())
if n==0: # 可以什么都不买
    print(1)
    exit()
cnt=0
for z in range(n):
    x=4*z/3-n
    y=(-7)*z/3+2*n
    if x>=0 and y >=0 and x%1==0 and y%1==0:
        cnt+=1
print(cnt)

''' 枚举法（如果用三层循环可能会超时）
n=int(input())
cnt=0
for i in range(0,n+1,3):
    for j in range(0,n-i+1):
        if i/3+j*5+(n-i-j)*3==n:
            cnt+=1
print(cnt)
'''