board = [[0 for i in range(5)] for j in range(5)]

n = int(input())
turn = 1
for _i in range(n):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = turn
    turn = 3 - turn
    for line in board:
        print(line)
    print()
