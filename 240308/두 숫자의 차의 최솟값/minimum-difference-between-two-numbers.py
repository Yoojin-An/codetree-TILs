nums = list(map(int, input().split()))
_min = 10
difference = 10
for index, num in enumerate(nums):
    for i in range(len(nums)):
        if i == index:
            print(111)
            difference = abs(num - nums[i])
            if difference < _min:
                _min = difference

print(difference)