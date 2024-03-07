nums = list(map(int, input().split()))
for i, value in enumerate(nums):
    if value % 3 == 0:
        answer_index = i - 1
        break
print(nums[answer_index])