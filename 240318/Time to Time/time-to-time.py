a, b, c, d = map(int, input().split())
hour = c - a
minute = d - b
if minute < 0:
    hour -= 1
    minute += 60

answer = (hour * 60) + minute
print(answer)