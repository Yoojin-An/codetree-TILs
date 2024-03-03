arr = []
while True:
    age = int(input())
    if not 20 <= age < 30:
      break
    arr.append(age)

print("{:.2f}".format(sum(arr)/len(arr)))