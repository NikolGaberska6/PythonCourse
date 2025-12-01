import random
num_numbers = int(input("Изберете колко числа да съдържа списъка: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]

max_number = max(list_of_nums)
print(max_number)