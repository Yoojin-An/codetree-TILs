n = int(input())
nums = list(map(int, input().split()))
k = int(input())

factors = []
multiples = [] 

for num in nums:
    if k % num == 0:
        factors.append(num)
    if num % k == 0:
        multiples.append(num)

print(sum(factors))
print(sum(multiples))