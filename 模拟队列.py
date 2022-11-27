from sys import stdin

q = [0] * 100000
head = tail = 0
M = int(input())
for l in stdin.readlines():
    l = l[:-1]
    if l[-1].isnumeric():
        q[tail] = int(l.split()[-1])
        tail += 1
    elif l == "pop":
        head += 1
    elif l == "empty":
        print("YES" if head == tail else "NO")
    elif l == "query":
        print(q[head])
