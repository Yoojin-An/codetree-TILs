n = int(input())
answer = []

def is_decimal(num) -> bool:
    answer = True
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            answer = False
            break
    return answer

for i in range(2, n + 1):
    if is_decimal(i):
        print(i, end=" ")