a,b=map(int,input().split(','))
for i in range(a,b+1):
    if i==(i//100)**3+(i//10%10)**3+(i%10)**3:
        print(i)