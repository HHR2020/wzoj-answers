s = input()
sec_len = 1
sec = s[0]
for i in range(1, len(s)):
    if s[i] == sec:
        sec_len += 1
    else:
        print(sec_len, sec, end=" ")
        sec, sec_len = s[i], 1
if s[-1] == sec:
    print(sec_len, sec)
