def power(base, exponent):
  if exponent == 0:
    return 1
  return base * power(base, exponent - 1)

a, b = map(int, input().split())
first_num = power(a, b)
second_num = power(b, a)

if first_num == second_num:
  print(0)
else:
  print(max([first_num, second_num]) - min([first_num, second_num]))