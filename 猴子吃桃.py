"""
def peach (n):
    if n==1:
        return 1
    else:
        return 2*(peach(n-1)+1)
a=int(input())
print(peach(a)%100007)
"""
a = int(input())
s = 1
for i in range(a - 1):
    s += 1
    s *= 2
print(s % 100007)
