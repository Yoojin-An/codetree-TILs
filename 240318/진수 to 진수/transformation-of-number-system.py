a, b = map(int, input().split())
n = input()
n = int(n, a)
if b == 2:
    n = bin(n).replace("0b", "")
elif b == 8:
    n = oct(n).replace("0o", "")
elif b == 16:
    n = hex(n).replace("0x", "")

print(n)