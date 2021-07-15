m,n=int(input()),int(input())
s=0
for i in range(m,n+1):
    if i%2==1:
        s+=i
print(s)