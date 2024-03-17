n = int(input())
lines = []
for i in range(n):
    lines.append(input())
condition = input()

length = 0
cnt = 0
for line in lines:
    if line.startswith(condition):
        length += len(line)
        cnt += 1

print(cnt, "{:.2f}".format(length / cnt))