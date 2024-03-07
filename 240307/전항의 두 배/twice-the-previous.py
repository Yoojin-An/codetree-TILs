n1, n2 = map(int, input().split())
print(n1, n2, end=" ")
for i in range(8):
    next_n = 2 * n1 + n2
    print(next_n, end=" ")
    n1, n2 = n2, next_n