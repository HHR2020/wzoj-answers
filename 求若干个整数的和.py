def parse(s):
    sign,num=1,0
    for ch in s:
        if '0'<=ch<='9':
            num=num*10+ord(ch)-48
        elif ch=='-':
            sign=-1
    return num*sign

a=parse(input())
b=0
while(a):
    b+=a
    a=parse(input())
print(b)