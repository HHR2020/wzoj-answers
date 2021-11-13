n, m = map(int, input().split())
l = []
while len(l) < n:
    l += input().split()
for i in range(m):
    x = input()
    while len(x) == 0:
        x = input()
    x = int(x)
    print(l[x - 1])
""" 正常做法
n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(m):
    x=int(input())
    print(l[x-1])
"""
