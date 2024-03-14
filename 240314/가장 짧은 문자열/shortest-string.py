arr = []

for i in range(3):
    arr.append(len(input()))

mininum = min(arr)
maximum = max(arr)

print(maximum - mininum)