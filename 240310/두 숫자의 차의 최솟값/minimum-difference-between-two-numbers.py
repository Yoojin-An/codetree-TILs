n = int(input())
numbers = list(map(int, input().split()))

# 초기 차이값을 무한대로 초기화한다.
min_diff = 100

# 리스트의 인접한 요소들의 차이를 계산하여 최소 차이를 찾습니다.
for i in range(n - 1):
    diff = numbers[i+1] - numbers[i]
    if diff < min_diff:
        min_diff = diff

# 최소 차이를 반환합니다.
print(min_diff)