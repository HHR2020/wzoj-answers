a = input().split()
b = {}
mkey = ""
mitem = 0
for item in a:
    c = ""
    for j in item:
        if "a" <= j <= "z":
            c += j
        elif "A" <= j <= "Z":
            c += chr(ord(j) + 32)
    if c in b:
        b[c] += 1
    else:
        b[c] = 1
for key, item in b.items():
    if item > mitem or item == mitem and key < mkey:
        mitem = item
        mkey = key
print(mkey, mitem)
