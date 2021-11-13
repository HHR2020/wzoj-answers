n = 0
for five in range(1, 20):
    for two in range(1, 50):
        one = 100 - five * 5 - two * 2
        if one >= 1:
            n += 1
            print(five, two, one)
        else:
            break
print(n)
