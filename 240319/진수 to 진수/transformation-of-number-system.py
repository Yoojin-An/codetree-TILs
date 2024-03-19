a, b = map(int, input().split())
n = int(input(), a) # n을 10진수로 변환
#n을 b진수로 변환
# n = format(n, f"0{b}").replace("0b", "").replace("0o", "").replace("0x", "")

if b == 2:
    n = bin(n).replace("0b", "")
elif b == 8:
    n = oct(n).replace("0o", "")
elif b == 16:
    n = hex(n).replace("0x", "")

print(n)