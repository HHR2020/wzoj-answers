s = input()
st = []
for c in s:
    if c == "(":
        st.append("(")
    elif c == ")":
        if st != [] and st[-1] == "(":
            st.pop()
        else:
            st.append(")")
if st == []:
    print("YES")
else:
    print("NO")
