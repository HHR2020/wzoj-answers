"""
def method(s):
    l=[]
    for i in range(4):
        l.append(int(s[i]))
    return (l[3]-l[2]-l[1]-l[0])>0
n=int(input())
m=list(map(method,input().split()))
cnt=0
for i in m:
    if i:
        cnt+=1
print(cnt)
"""
n = int(input())
m = input().split()
cnt = 0
for a in m:
    if int(a[3]) - int(a[2]) - int(a[1]) - int(a[0]) > 0:
        cnt += 1
print(cnt)
