x=int(input())
a=x//100
b=x//10%10
c=x%10
if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
print(a*100+b*10+c)