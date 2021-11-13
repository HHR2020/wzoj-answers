n = int(input())
ans = 0
prime = [True] * 1001
for i in range(2, 1001):
    if prime[i] == True:
        k = 2 * i
        while k <= 1000:
            prime[k] = False
            k += i
for i in range(3, n - 1):
    if prime[i] and prime[i + 2]:
        ans += 1
        print(i, i + 2)
print(ans)
