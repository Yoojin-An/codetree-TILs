letter = input()
ASCII = ord(letter)
if letter != 'a': 
    pre_letter = chr(ASCII - 1)
else:
    pre_letter = 'z'
print(pre_letter)