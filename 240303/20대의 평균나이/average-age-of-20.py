arr = []
while True:
    age = int(input())
    if age < 20 or age > 30:
        break
    arr.append(age)

print("{:.2f}".format(sum(arr)/len(arr)))