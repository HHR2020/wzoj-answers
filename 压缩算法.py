a=input()
ans=""
n=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        n+=1
    else:
        ans+=str(n)+a[i-1]
        n=1
ans+=str(n)+a[-1:]
print(ans)