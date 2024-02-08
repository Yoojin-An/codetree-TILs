def calculation(a, b):
    small_num = min(a, b) + 10
    big_num = max(a, b) * 2

    print(small_num, big_num, end = ' ')

a, b = map(int, input().split())
calculation(a, b)