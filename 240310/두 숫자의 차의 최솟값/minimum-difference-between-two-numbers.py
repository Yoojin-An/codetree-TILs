n = int(input())
numbers = list(map(int, input().split()))

# 초기 차이값을 무한대로 초기화
min_diff = float('inf')

for i in range(n - 1):
    diff = numbers[i+1] - numbers[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)
