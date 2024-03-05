n = int(input())

num = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 != 0:
            print(num, end=" ")
            if j != n:
                num += 1
            else:
                num += 2
        else:
            print(num, end=" ")
            if j != n:
                num += 2
            else:
                num += 1
    print()