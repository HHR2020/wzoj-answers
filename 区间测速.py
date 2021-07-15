s=float(input())
t=float(input())
t=t/3600
v=s/t
if v<=100:
    print("no")
elif v<120:
    print("<20%")
    print("%.2f"%v)
elif v<150:
    print("<50%")
    print("%.2f"%v)
elif v<170:
    print("<70%")
    print("%.2f"%v)
else:
    print(">=70%")
    print("%.2f"%v)