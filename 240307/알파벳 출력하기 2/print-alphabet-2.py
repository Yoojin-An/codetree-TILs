n = int(input())

num = ord('A')
for i in range(n):
    for j in range(n):
        if i <= j:
            print(chr(num), end=" ")
            num += 1
        else:
            print(" ", end=" ")
    print()