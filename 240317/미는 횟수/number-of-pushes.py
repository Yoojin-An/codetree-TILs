def shifted_count(string, comparision_string):
    n = 0
    while n < len(string):
        string = string[-1] + string[:-1]
        n += 1
        if string == comparision_string:
            break
    return n

A = input()
B = input()

n = shifted_count(A, B)

if n == len(A) - 1:
    print(-1)
print(n)