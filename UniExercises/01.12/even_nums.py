import random
def num_even_numbers(list_of_nums):
    num_even_nums = 0
    for num in list_of_nums:
        if num % 2 == 0:
            num_even_nums += 1
    print(num_even_nums)

num_numbers = int(input("Въведете колко числа искате да съдържа списъка ви: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]
print(list_of_nums)
num_even_numbers(list_of_nums)