import copy
a, b, c = 5, 6, 7
temp = a
a = c
c = b
b = temp
print(a, b, c, sep = "\n")