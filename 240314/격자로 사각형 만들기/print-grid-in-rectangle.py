n = int(input())

grid = [[0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            grid[i][j] = 1
        else:
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1] + grid[i - 1][j - 1]

for row in grid:
    for col in row:
        print(col, end=" ")
    print()