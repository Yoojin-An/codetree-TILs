A = input()
B = input()

answer = 0

for i in range(len(A) - 1):
    if A[i:i + 2] == B:
        answer += 1

print(answer)