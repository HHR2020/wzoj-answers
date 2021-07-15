n=int(input())
plateau=[]
while len(plateau)<n:
    plateau+=input().split()
status=""
length=0
maxlen=0
for i in plateau:
    if status==i:
        length+=1
    else:
        status=i
        if length>maxlen:
            maxlen=length
        length=1
if length>maxlen:
    maxlen=length
print(maxlen)
