n = int(input())

for i in range(1, 2 * n - 3):
    print(" " * (n - i - 1), "* " * i)
print("* " * n)
for i in range(2 * n - 4, 0, - 1):
    print(" " * (n - i - 1), "* " * i)