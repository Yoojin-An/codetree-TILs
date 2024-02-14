def in_range(n, x, y):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1 

def move(grid, n, r, c):
    r -= 1
    c -= 1
    curr_value = grid[r][c]
    next_value = 0
    answer = [curr_value]
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for x, y in zip(dxs, dys):
        next_x, next_y = r + x, c + y
        if in_range(n, next_x, next_y):
            next_value = grid[next_x][next_y]
        if next_value > curr_value:
            answer.append(next_value)
            curr_value = next_value
            r, c = next_x, next_y
    return answer

n, r, c = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

answer = move(grid, n, r, c)

for i in answer:
    print(i, end = " ")