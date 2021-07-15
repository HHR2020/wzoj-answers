'''
a=input()
a=a[::-1]
s=""
for i in range(len(a)):
    s=s+a[i]
    if (i+1)%3==0 and i+1!=len(a):
        s=s+","
s=s[::-1]
print(s)
'''
a=int(input())
print(format(a,','))
