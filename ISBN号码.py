isbn = input()
s = list(isbn)
s.remove("-")
s.remove("-")
s.remove("-")
if s[9] == "X":
    s[9] = "10"
s = list(map(int, s))
add = 0
for i in range(9):
    add += (i + 1) * s[i]
add %= 11
if add == s[9]:
    print("Right")
else:
    for i in range(9):
        print(s[i], end="")
        if i == 0 or i == 3 or i == 8:
            print("-", end="")
    if add == 10:
        print("X")
    else:
        print(add)
