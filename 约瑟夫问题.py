n, m = map(int, input().split())
people = [0] * n
out = 0
position = 0
f = 0
while out < n:
    if people[position] == 0:
        if f == m - 1:
            people[position] = 1
            print(position + 1, end=" ")
            out += 1
            f = 0
        else:
            f += 1
    position = (position + 1) % n
