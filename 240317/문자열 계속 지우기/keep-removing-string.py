A = input()
B = input()

while True:
    if B in A:
        A = A.replace(B, "")
    else:
        break

print(A)