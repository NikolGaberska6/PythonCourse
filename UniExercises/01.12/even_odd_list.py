import random
num_numbers = int(input("Изберете колко числа да съдържа списъка: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]

even_list = []
odd_list = []
for num in list_of_nums:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(even_list)
print(odd_list)