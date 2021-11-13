for i in range(6):
    champion = [0] * 6
    champion[i] = 1
    w = champion[0] or champion[1]
    x = not champion[2]
    y = not champion[3] or champion[4] or champion[5]
    z = champion[3] or champion[4] or champion[5]
    if w + x + y + z == 1:
        print(chr(ord("A") + i))
