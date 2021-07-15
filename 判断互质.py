'''
def gcd(a,b):
    if a==1 or b==1:
        print("Yes")
    elif a%b==0 or b%a==0:
        print("No")
    else:
        gcd(b,a%b)
m,n=map(int,input().split())
gcd(m,n)
'''
m,n=map(int,input().split())
while m!=1 and n!=1 and m%n!=0 and n%m!=0:
    m,n=n,m%n
if m==1 or n==1:
    print("Yes")
elif m%n==0 or n%m==0:
    print("No")
