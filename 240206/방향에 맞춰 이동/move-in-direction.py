def orient_to_index(orient):
  if orient == 'W':
    orient = 0
  elif orient == 'S':
    orient = 1 
  elif orient == 'N':
    orient = 2
  elif orient == 'E':
    orient = 3
  return orient

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
nx, ny = 0, 0
n = int(input())
for i in range(n):
    orient, distance = input().split()
    orient = orient_to_index(orient)
    distance = int(distance)
    nx += dx[orient] * distance
    ny += dy[orient] * distance

print(nx, ny, end = " ")