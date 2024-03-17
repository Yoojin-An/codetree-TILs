def shift(string, condition, cnt):
    if condition == 'L':
        for i in range(cnt):
            string = string[1:] + string[0]
    elif condition == 'R':
        for i in range(cnt):
            string = string[-1] + string[1:]
    else:
        pass
    return string

string = input()
direction_to_move = input()
len_L = direction_to_move.count("L")
len_R = direction_to_move.count("R")

if len_L > len_R:
    condition = 'L'
elif len_L < len_R:
    condition = 'R'
else:
    condition = None

cnt = abs(len_L - len_R)

shifted_string  = shift(string, condition, cnt)

print(shifted_string)