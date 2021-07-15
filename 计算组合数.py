def c(n,m):
    print(f(n)//(f(m)*f(n-m)))

def f(n):
    if n==0:
        return 1
    for i in range(1,n):
        n*=i
    return n

a,b=map(int,input().split())
c(a,b)