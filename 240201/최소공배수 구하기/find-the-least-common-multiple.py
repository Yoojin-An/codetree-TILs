def the_least_common_multiple(n, m): 
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            return i

n, m = map(int, input().split())
lcm = the_least_common_multiple(n, m)
print(lcm)