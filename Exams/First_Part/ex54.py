import random
nums = []
for i in range(30):
    number = random.randint(-50, 150)
    nums.append(number)
    print(f"Успешно добавихте числото {number} в листа!")

sum_of_el = nums[2] + nums[6] + nums[9]
print(f"Сумата от елементите на 2, 6 и 9ти индекс е: {sum_of_el}.")
max_el = max(nums)
print(f"Най-голямата стойност в списъка е: {max_el}.")

nums_even = []
for number in nums:
    if number % 2 == 0:
        nums_even.append(number)
        print(f"Успешно добавихте числото {number} във втория лист!")

if len(nums_even) > 0:
    diff = len(nums) - len(nums_even)
    print(f"Разликата в дължините на двата списъка е: {diff}.")

    first_el = nums_even[0]
    last_el = nums_even[-1]
    nums_even.remove(first_el)
    nums_even.remove(last_el)
    print("Изтрихте първия и последния елемент от листа!")

else:
    print("В първия лист няма четни числа!")
    print("Втория лист nums_even е празен!")