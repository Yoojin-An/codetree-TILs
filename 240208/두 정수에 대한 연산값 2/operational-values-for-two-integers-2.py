def calculation(a, b):
    # 인자 순서와 반환값 순서가 일치해야 함
    if a < b:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    return a, b


a, b = map(int, input().split())
a, b = calculation(a, b)
print(a, b, end = ' ')