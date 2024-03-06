n = int(input())

num = ord('A')
last_num = ord('Z')
for i in range(n):
    for j in range(n):
        if i <= j:
            print(chr(num), end=" ")
            num += 1
            if num > last_num:
                num = ord('A')
        else:
            print(" ", end=" ")
    print()