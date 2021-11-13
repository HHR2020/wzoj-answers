def abort():
    print("Failed")
    exit()


encrypted, original = input(), input()
dic = {}
for i in range(len(encrypted)):
    if encrypted[i] in dic and dic[encrypted[i]] != original[i]:
        abort()
    dic[encrypted[i]] = original[i]
if len(dic) < 26:
    abort()
for i in range(26):
    if not chr(ord("A") + i) in dic.values():
        abort()
word = input()
for i in word:
    if not i in dic:
        abort()
    print(dic[i], end="")
