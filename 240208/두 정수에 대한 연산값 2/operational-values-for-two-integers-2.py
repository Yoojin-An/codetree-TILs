def calculation(a, b):
    small_num = min(a, b) + 10
    big_num = max(a, b) * 2

    print(big_num, small_num, end = ' ')

a, b = map(int, input().split())
calculation(a, b)