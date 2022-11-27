s = input().split()
st = []
for i in s:
    if i[-1].isdecimal():
        st.append(int(i))
    else:
        b = int(st.pop())
        a = int(st.pop())
        if i == "+":
            st.append(a + b)
        elif i == "-":
            st.append(a - b)
        elif i == "*":
            st.append(a * b)
        elif i == "/":
            st.append(a // b)
print(st[0])
