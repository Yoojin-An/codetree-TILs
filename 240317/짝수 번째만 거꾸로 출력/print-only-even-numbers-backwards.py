line = input()
answer = []
for index, string in enumerate(line):
    if index % 2 != 0:
        answer.append(string)

answer.reverse()
print("".join(answer))