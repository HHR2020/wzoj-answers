a = [list(map(int, input().split())) for i in range(5)]
find = False
for i in range(5):
    # 实现从第i行找出最大值val和对应列pos
    pos = 0
    val = a[i][pos]
    for j in range(1, 5):
        if a[i][j] > val:
            val = a[i][j]
            pos = j

    # 实现val是否是第pos的最小值
    flag = True
    for j in range(5):
        if a[j][pos] < val:
            flag = False

    if flag:
        find = True
        print(i + 1, pos + 1, val)
        break
if not find:
    print("not found")
