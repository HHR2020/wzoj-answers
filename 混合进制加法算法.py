s = input()[:-1].split("+")
scales = {"B": 2, "H": 16, "D": 10}
digits = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


def t(n):
    scale = scales[n[-1]]
    n = n[:-1]
    ans = 0
    while n:
        ans = ans * scale + digits[n[0]]
        n = n[1:]
    return ans


print(sum(map(t, s)))
