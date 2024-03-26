arr = []
n = int(input())
for i in range(n):
    command = input()

    if command.startswith('push_back') :
        command, value = command.split()
        arr.append(int(value))
    elif command == 'pop_back':
        if arr:
            arr.pop()
    elif command == 'size':
        print(len(arr))
    elif command.startswith('get'):
        command, index = command.split()
        print(arr[int(index) - 1])