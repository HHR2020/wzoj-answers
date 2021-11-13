s = input()
for i in s:
    if i.isupper():
        print(chr((ord(i) - ord("A") + 4) % 26 + ord("A")), end="")
    elif i.islower():
        print(chr((ord(i) - ord("a") + 4) % 26 + ord("A")), end="")
    elif i.isnumeric():
        print(chr((ord(i) - ord("0") + 8) % 10 + ord("0")), end="")
    else:
        print(i, end="")
