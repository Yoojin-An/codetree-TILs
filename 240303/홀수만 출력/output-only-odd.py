a, b = map(int, input().split())
arr = []
for i in range(a, b + 1):
    if i % 2 != 0:
        arr.append(i)
arr.sort()
for i in arr:
    print(i, end = " ")