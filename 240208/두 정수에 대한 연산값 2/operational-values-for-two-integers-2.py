def calculation(a, b):
    small_num = min(a, b) + 10
    big_num = max(a, b) * 2

    return small_num, big_num

a, b = map(int, input().split())
small_num, big_num = calculation(a, b)
print(small_num, big_num, end = ' ')