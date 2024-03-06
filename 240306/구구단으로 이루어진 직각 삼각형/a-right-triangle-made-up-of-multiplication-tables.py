n = int(input())

for i in range(1, n + 1):
    num = 1
    for j in range(1, n + 1):
        if i <= j:
            print(f"{i} * {num} = {i * num}", end="")
            num += 1
            if num <= n - i + 1: # 출력되는 연산의 수
                print(" / ", end="")
    print()