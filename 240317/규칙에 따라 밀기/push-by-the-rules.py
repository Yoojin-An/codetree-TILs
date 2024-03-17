def shift(string, condition, cnt):
    for i in range(cnt):
        if condition == 'L':
            string = string[1:] + string[0]
        elif condition == 'R':
            string = string[-1] + string[1:]
    return string

string = input()
direction_to_move = input()
len_L = direction_to_move.count("L")
len_R = direction_to_move.count("R")

if len_L > len_R:
    condition = 'L'
else:
    condition = 'R'
cnt = abs(len_L - len_R)
shifted_string  = shift(string, condition, cnt)

print(shifted_string)