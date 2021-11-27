# 输出第一行和第二行
print([1])
line = [1, 1]
print(line)
# 从第三行开始的其他行
for i in range(2, 6):
    r = []  # 初始化r
    # 按规律生成该行除两端之外的数字
    for j in range(1, i):
        r.append(line[j - 1] + line[j])  # append函数用于在列表末尾添加新的对象
    # 把两端的数字连接上
    line = [1] + r + [1]
    print(line)
