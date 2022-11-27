N = int(input())
st = []
for n in map(int, input().split()):
    if st == []:
        st.append(n)
        print(-1, end=" ")
        continue
    while st != [] and n <= st[-1]:
        st.pop()
    if st == []:
        st.append(n)
        print(-1, end=" ")
    else:
        print(st[-1], end=" ")
        st.append(n)
