n, m = map(int, input().split())
first_grid = []
second_grid = []
new_grid = [[0] * m for _ in range(n)]
for i in range(n):
    first_grid.append(list(map(int, input().split())))
for i in range(n):
    second_grid.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if first_grid[i][j] != second_grid[i][j]:
            new_grid[i][j] = 1

for row in new_grid:
    for col in row:
        print(col, end=" ")
    print()