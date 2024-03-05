n = int(input())

for i in range(n, 0, -1):
    num = i
    for j in range(n, 0, -1):
        if i <= j:
            print(num , end = " ")
            num += 1
    print()