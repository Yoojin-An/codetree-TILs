a, b, c = map(int, input().split())
arr = [a, b, c]
print(sum(arr)) 
print(int(sum(arr)/3))
print(int(sum(arr) - sum(arr)/3))