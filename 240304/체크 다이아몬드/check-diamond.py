n = int(input())

for i in range(1, 2 * n - 2):
    print(" " * (n - i), "* " * i)
for i in range(2 * n - 4, 0, - 1):
    print(" " * (n - i), "* " * i)