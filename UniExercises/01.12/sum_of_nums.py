import random
def sum_of_nums(list_of_nums):
    sum = 0
    for num in list_of_nums:
        if num > 10:
            sum += num
    print(sum)


num_numbers = int(input("Въведете колко числа искате да съдържа листа: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]
print(list_of_nums)
sum_of_nums(list_of_nums)