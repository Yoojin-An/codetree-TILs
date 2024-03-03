a, b = map(int, input().split())
comm_factors = []
for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        comm_factors.append(i)
if comm_factors:
    print(1)
else:
    print(0)