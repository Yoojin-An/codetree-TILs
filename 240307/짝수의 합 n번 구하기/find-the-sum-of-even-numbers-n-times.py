n = int(input())
result = []
for i in range(n):
    a, b = map(int, input().split())
    one_sum = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            one_sum += i
    result.append(one_sum)

for _ in result:
    print(_)