import random
def find_max_num(list_of_nums):
     max_num = list_of_nums[0]
     for num in list_of_nums:
         if num > max_num:
             max_num = num
     print(max_num)

num_numbers = int(input("Въведете колко числа искате да съдържа листа: "))
list_of_nums = [random.randint(1, 100) for _ in range(num_numbers)]
print(list_of_nums)
find_max_num(list_of_nums)