nums = list(map(int, input().split()))
n = [0] * (2**15)
for i in nums:
    n[i] += 1
for i in range(len(n)):
    while n[i] != 0:
        print(i, end=" ")
        n[i] -= 1
