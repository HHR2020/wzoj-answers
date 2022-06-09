plaintext = list(input())
pointer = 0
n = 0
nth = 0
chipertext = ""
while n < len(plaintext):
    if plaintext[pointer]:
        if nth == 0:
            print(plaintext[pointer], end="")
            plaintext[pointer] = False
            n += 1
        nth = 1 - nth
    pointer = (pointer + 1) % len(plaintext)
