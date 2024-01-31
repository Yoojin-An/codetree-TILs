def is_all_positive(grid, x1, y1, x2, y2):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if grid[i][j] <= 0:
                return False
    return True

def get_max_rectangle(grid, n, m):
    max_area = 0
    for y1 in range(n):
        for x1 in range(m):
            for y2 in range(y1, n):
                for x2 in range(x1, m):
                    if is_all_positive(grid, x1, y1, x2, y2):
                        area = (y2 - y1 + 1) * (x2 - x1 + 1)
                        max_area = max(area, max_area)
    return max_area

n, m = map(int, input().split())
grid = []
for i in range(1, n + 1):
    grid.append(list(map(int, input().split())))

continuous_positive_nums = get_max_rectangle(grid, n, m)
if continuous_positive_nums >= 2:
    print(continuous_positive_nums)
else:
    print(-1)