s=input()
if len(s)<8:
    print("no")
    exit()
n,a,o=0,0,0
for ch in s:
    if ch.isdecimal():
        n=1
    elif ch.isalpha():
        a=1
    else:
        o=1
if n+a+o==1:
    print("weak")
elif n+a+o==2:
    print("moderate")
elif n+a+o==3:
    print("strong")