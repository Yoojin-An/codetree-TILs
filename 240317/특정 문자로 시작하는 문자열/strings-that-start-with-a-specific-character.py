n = int(input())
lines = [input() for _ in range(n)]
condition = input()

length = 0
cnt = 0
for line in lines:
    if line.startswith(condition):
        length += len(line)
        cnt += 1

print(cnt, "{:.2f}".format(length / cnt))