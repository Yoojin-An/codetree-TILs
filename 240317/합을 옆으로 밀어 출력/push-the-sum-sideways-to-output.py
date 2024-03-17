n = int(input())
sum_of_nums = 0
for _ in range(n):
    sum_of_nums += int(input())

answer = str(sum_of_nums)[1:-1] + str(sum_of_nums)[0]