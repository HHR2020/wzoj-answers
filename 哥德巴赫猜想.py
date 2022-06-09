NMAX = 2**15 + 1
primes = [True] * (NMAX + 1)
primes[0] = primes[1] = False
for i in range(2, NMAX + 1):
    if primes[i] == True:
        for j in range(2 * i, NMAX + 1, i):
            primes[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            cnt += 1
    print(cnt)
