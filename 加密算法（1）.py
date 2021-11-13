rs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
s = input().strip()
ans = ""
for i in range(0, len(s), 3):
    a1 = ord(s[i])
    a2 = ord(s[i + 1])
    a3 = ord(s[i + 2])
    b1 = a1 // 4
    b2 = a1 % 4 * 16 + a2 // 16
    b3 = a2 % 16 * 4 + a3 // 64
    b4 = a3 % 64
    ans = ans + rs[b1] + rs[b2] + rs[b3] + rs[b4]
print(ans)
"""
import base64
print(base64.b64encode(input().strip().encode()).decode())
"""
