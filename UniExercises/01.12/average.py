import random
num_numbers = int(input("Изберете колко числа да съдържа списъка: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]

average = sum(list_of_nums)/len(list_of_nums)
print(average)

for num in list_of_nums:
    if num > average:
        print(num)