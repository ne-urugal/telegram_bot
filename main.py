import math

numbers = list(input())

def square_sum(numbers):
    for n in numbers:
        sq_num = n ** 2 + 3
        sum_sq = sq_num + sq_num
        return sum_sq

print(square_sum)