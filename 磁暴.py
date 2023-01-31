from sys import stdin

M = int(input())
n = [int(i) for i in stdin.readlines()]
n.pop()
st = []
ans = []
N = len(n)
for i in range(N):
    if st and i - st[0][0] > M - 1:
        st = st[1:]
    while st and st[-1][1] < n[i]:
        st.pop()
    st.append([i, n[i]])
    if i >= M - 1:
        ans.append(st[0][1])
print(*ans, sep="\n")
