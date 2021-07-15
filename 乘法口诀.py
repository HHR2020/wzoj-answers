n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(i*j),end=" ")
    print()