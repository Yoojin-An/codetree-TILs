n = int(input())
upper_stars = []

for i in range(1, n + 1):
    if i % 2 != 0:
        num = n
        n -= 1
    else:
        num = n // 2
    stars = "* " * num
    print(stars)
    upper_stars.append(stars)

lower_stars = list(reversed(upper_stars))
for i in lower_stars:
    print(i)