n = int(input())
city = "B"
limit = {"1": "19", "2": "28", "3": "37", "4": "46", "5": "50", "6": "", "7": ""}
cars = [[s for s in input().split()] for _i in range(n)]


def last_number(plate: str):
    if plate == "":
        return False
    elif plate[-1].isnumeric():
        return plate[-1]
    else:
        return last_number(plate[:-1])


print("license number owner's name")

for car in cars:
    if car[0][4] != "B" or (
        last_number(car[0]) and last_number(car[0]) in limit[car[-1]]
    ):
        print(*car[0:2])
