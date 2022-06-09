for i in range(2, 85):
    if 168 % i == 0:
        j = 168 // i
        if i > j and i % 2 == 0 and j % 2 == 0:
            m = (i + j) // 2
            n = (i - j) // 2
            x = n**2 - 100
            print(x)
