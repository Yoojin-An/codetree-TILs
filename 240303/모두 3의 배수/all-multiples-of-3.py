nums = []
for i in range(5):
    n = int(input())
    nums.append(n)

satisfied = True
for i in nums:
    if i % 3 != 0:
        satisfied = False
        break

if satisfied:
    print(1)
else:
    print(0)