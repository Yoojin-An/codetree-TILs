n = int(input())

for i in range(1, 2 * n -n):
    print(" " * (n - i - 1), "* " * i)
print("* " * n)
for i in range(2 * n - 1 - n, 0, - 1):
    print(" " * (n - i - 1), "* " * i)