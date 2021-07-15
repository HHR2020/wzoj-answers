import math
def left(a):#返回空格子数
    n=0
    for i in range(len(a)):
        if a[i]==0:
            n+=1
    return n
def maxblank(a):#返回最长的空区域
    maxn,n=0,0
    for i in range(len(a)):
        if a[i]==0:
            n+=1
        else:
            if n>maxn:
                maxn=n
            n=0
    if n>maxn:
        maxn=n
    return maxn
def fillblank(a,x):#向a的空区域居中连续放置x个
    n=0
    for i in range(len(a)+1):
        if i==len(a):
            return put(a,i-n,i,x)
            break
        if a[i]==0:
            n+=1
        else:
            if n>=x:
                return put(a,i-n,i,x)#在a的索引[i-n,i)间居中放置x个物品
            else:
                n=0
                continue
def put(a,l,r,x):#[l,r)
    length=r-l#区间长度
    for i in range(l+math.floor((length-x)/2),r-math.ceil((length-x)/2)):
        a[i]=1
    return l+math.floor((length-x)/2),r-math.ceil((length-x)/2) #左闭右开区间
def printnum(L,R,depth):#floor[depth]就是要操作的层
    for i in range(depth*10+(L+1),depth*10+(R+1)):
        print(i,end=" ")
    print()

group=list(map(int,input().split()))
floor=[None]*5
for i in range(5):
    floor[i]=[0]*10

for i in range(len(group)):
    #整体放置
    for j in range(len(floor)):
        if group[i]<=maxblank(floor[j]):
            l,r=fillblank(floor[j],group[i])
            printnum(l,r,j)
            group[i]=0
            break
    if group[i]==0:
        continue
    #零散放置
    for j in range(len(floor)):
        for k in range(len(floor[j])):
            if floor[j][k]==0 and group[i]>0:
                floor[j][k]=1
                print(j*10+k+1,end=" ")
                group[i]-=1
    print()
'''
import math
group=list(map(int,input().split()))
floor=[None]*5
for i in range(5):
    floor[i]=[0]*10
for i in range(9):
    for j in range(5):
        maxn,n=0,0
        for k in range(10):
            if floor[j][k]==0:
                n+=1
            else:
                if n>maxn:
                    maxn=n
                n=0
        if n>maxn:
            maxn=n
        if group[i]<=maxn:
            b=0 # 空区间长度
            l,r=0,0 # [l,r)空区间
            for k in range(11):
                if k==10:
                    l,r=10-b,10
                    break
                if floor[j][k]==0:
                    b+=1
                elif b<group[i]:
                    b=0
                else:
                    l,r=k-b,k
                    break
            # 接下来改变格子的状态
            L,R=l+math.floor((r-l-group[i])/2),r-math.ceil((r-l-group[i])/2)
            for k in range(L,R):
                floor[j][k]=1
            # 接下来打印
            for k in range(j*10+(L+1),j*10+(R+1)):
                print(k,end=" ")
            print()
            group[i]=0
            break
    if group[i]==0:
        continue
    # 零散放置
    for j in range(5):
        for k in range(10):
            if floor[j][k]==0 and group[i]>0:
                floor[j][k]=1
                print(j*10+k+1,end=" ")
                group[i]-=1
    print()
'''