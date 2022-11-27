N = int(input())
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
matrix = [[False for j in range(N)] for i in range(N)]


def draw(nth: int, d, row, col):
    matrix[row][col] = nth
    if nth == N**2:
        print(*matrix, sep="\n")
        return

    nextrow = row + direction[d][0]
    nextcol = col + direction[d][1]
    if nextrow == N or nextcol == N or matrix[nextrow][nextcol] != False:
        d = (d + 1) % 4
        nextrow = row + direction[d][0]
        nextcol = col + direction[d][1]
        draw(nth + 1, d, nextrow, nextcol)
    else:
        draw(nth + 1, d, nextrow, nextcol)


draw(1, 0, 0, 0)
