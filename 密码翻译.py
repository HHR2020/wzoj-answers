a = input()
for i in a:
    if "a" <= i <= "y" or "A" <= i <= "Y":
        print(chr(ord(i) + 1), end="")
    elif i == "z":
        print("a", end="")
    elif i == "Z":
        print("A", end="")
    else:
        print(i, end="")
