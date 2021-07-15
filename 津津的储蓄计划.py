m=[0]
save=0
left=0
for i in range(12):
    m.append(int(input()))
for i in range(1,13):
    left=300+left-m[i]
    if left<0:
        print("-"+str(i))
        exit()
    elif left>=100:
        save+=left//100*100
        left=left%100
print(int(save*1.2+left))