ticket = ("free", "half-price ticket", "full ticket")
height = float(input())
if height < 1.2:
    print(ticket[0])
elif 1.2 <= height < 1.5:
    print(ticket[1])
else:
    print(ticket[2])
