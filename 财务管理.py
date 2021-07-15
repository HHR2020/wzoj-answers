money=[]
s=0
for _i in range(12):
    money.append(float(input()))
for a in money:
    s+=a
print("$"+"%.2f"%(s/12))