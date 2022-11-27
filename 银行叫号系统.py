q = [i for i in range(1, 1001)]
head = tail = 0

x = int(input())
while x != 3:
    if x == 1:
        tail += 1
        print(tail - head)
    else:
        if head == tail:
            print("empty")
        else:
            print(q[head])
            head += 1
    x = int(input())
