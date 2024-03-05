a, b = map(int, input().split())

for i in range(2, 9, 2):
    line = ""
    for j in range(b, a - 1, -1):
        line += f"{j} * {i} = {i*j} / "
    print(line[: -2])