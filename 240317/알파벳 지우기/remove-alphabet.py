first_string = input()
second_string = input()
first_digit = ""
second_digit = ""

for i in first_string:
    if i.isdigit():
        first_digit += i

for i in second_string:
    if i.isdigit():
        second_digit += i

answer = int(first_digit) + int(second_digit)

print(answer)