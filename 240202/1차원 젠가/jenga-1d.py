def del_elements(arr, s, e):
    del arr[s-1:e]
    return arr

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

del arr[s1-1:e1]
del arr[s2-1:e2]

print(len(arr))
for i in arr:
    print(i)