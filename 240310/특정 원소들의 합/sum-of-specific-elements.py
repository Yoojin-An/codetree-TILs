grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))

answers = []
for row in range(4):
    for col in range(4):
        if row >= col:
            answers.append(grid[row][col])

print(sum(answers))