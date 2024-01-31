def recursive_call(n):
    if n == 0:
        return
    print("Coding is my favorite hobby!")
    return recursive_call(n-1)

n = int(input())
recursive_call(n)