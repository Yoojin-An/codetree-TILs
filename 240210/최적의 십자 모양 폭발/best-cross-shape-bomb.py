from copy import deepcopy

def explode(grid, row_idx, col_idx):
    value = grid[row_idx][col_idx]
    explosion_absolute = value - 1
    n = len(grid)
    
    # Explode horizontally
    for j in range((col_idx - (explosion_absolute)), (col_idx + (explosion_absolute) + 1)):
        if 0 <= j <= n - 1:
            grid[row_idx][j] = 0

    # Explode vertically
    for i in range((row_idx - (explosion_absolute)), (row_idx + (explosion_absolute) + 1)):
        if 0 <= i <= n - 1:
            grid[i][col_idx] = 0
    
    return grid

def after_gravity(grid):
    BLANK = 0
    n = len(grid)
    # 시계 반대방향으로 90도 회전해서 생각하기(열 -> 행)
    rotated_minus_90_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_minus_90_grid[n-1-j][i] = grid[i][j]
    
    # grid에 중력 작용: rotated_minus_90_grid에서 BLANK인 부분을 제외하고 오른쪽 정렬
    aligned_to_right_grid = [[0] * n for _ in range(n)]
    # for i, row in enumerate(rotated_minus_90_grid):
    for i, row in enumerate(rotated_minus_90_grid):
        temp_col = n - 1
        for j in range(n - 1, -1, -1):
            if row[j] != 0:
                aligned_to_right_grid[i][temp_col] = rotated_minus_90_grid[i][j]
                temp_col -= 1
    
    # dropped_grid를 시계방향으로 90도 회전해서 반환
    dropped_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dropped_grid[j][n-1-i] = aligned_to_right_grid[i][j]
    
    return dropped_grid

def count_couple(grid):
    global max_count
    count = 0
    n = len(grid)
    for i, row in enumerate(grid):
        for j, spot in enumerate(row):
            if spot != 0:
                if j < n - 1 and row[j] == row[j + 1]:
                    count += 1
                if j < n and i < n - 1 and row[j] == grid[i + 1][j]:
                    count += 1 
    max_count = max(count, max_count)

n = int(input())
max_count = 0 # count_couple 호출 시마다 갱신

# grid 생성
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

# 폭발 -> 중력 작용 -> 인접한 곳끼리 숫자가 동일한 쌍의 수 세기
for i, row in enumerate(grid):
    for j, spot in enumerate(row):
        copied_grid = deepcopy(grid)
        exploded_grid = explode(copied_grid, i, j)
        dropped_grid = after_gravity(exploded_grid)
        count_couple(dropped_grid)

print(max_count)