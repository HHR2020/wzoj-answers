i = 1
while i:
    fish = i
    for j in range(4):
        if fish % 4 == 0 and (fish - 1) % 5 == 0:
            fish = fish // 4 * 5 + 1
        else:
            fish = 0
            break
    if fish != 0:
        print(fish)
        break
    i += 1
