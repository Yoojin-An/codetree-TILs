a, b = map(int, input().split())

remainders = {}
answer = 0

while True:
    remainder = str(a % b)
    if remainder not in remainders:
        remainders[remainder] = 0
    remainders[remainder] += 1
    a = a // b
    if a <= 1:
        break

# 나머지가 등장한 횟수만 리스트에 담는다.
values = remainders.values()
for i in values:
    answer += i ** 2 # 등장한 횟수를 제곱해서 더하기

print(answer)