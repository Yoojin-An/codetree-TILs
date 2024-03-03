phone_num = input()
separated_phone_num = phone_num.split("-")
mid_num = separated_phone_num[1]
last_num = separated_phone_num[2]
new_phone_num = f"{separated_phone_num[0]}-{last_num}-{mid_num}"
print(new_phone_num)