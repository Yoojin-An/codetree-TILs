string = list(input())
first_letter = string[0]
second_letter = string[1]

for index, letter in enumerate(string):
    if letter == second_letter:
        string[index] = first_letter

print("".join(string))