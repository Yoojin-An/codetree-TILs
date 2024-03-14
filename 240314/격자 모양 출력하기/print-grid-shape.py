n, m = map(int, input().split())

grid = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    row, col = map(int, input().split())
    grid[row - 1][col - 1] = row * col

for i in grid:
    for j in i:
        if j > 0:
            print(j, end=" ")
        else:
            print(0, end=" ")
    print()