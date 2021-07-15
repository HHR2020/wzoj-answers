a=float(input())
if a<250:
    print("%.2f"%a)
elif a<500:
    print("%.2f"%(a*0.95))
elif a<1000:
    print("%.2f"%(a*0.90))
elif a<2000:
    print("%.2f"%(a*0.85))
else:
    print("%.2f"%(a*0.80))