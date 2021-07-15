import math
n=int(input())
if n==1:
    print(0)
    exit()
s=1
for i in range(2,math.ceil(n**0.5)):
    if n%i==0:
        s+=n/i+i
if n**0.5%1==0:
    s+=n**0.5
print(int(s))